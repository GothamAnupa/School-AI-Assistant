import streamlit as st
import os
import sys
from dotenv import load_dotenv

# 1. Load environment variables from .env file
load_dotenv()

# 2. Tell Python where to find the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# 3. LangChain & Modular Imports
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.config import DB_DIR, GROQ_MODEL
from src.embedder import get_embedding_model
from src.guardrails import check_input_safety, check_output_safety

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="School AI Assistant", page_icon="🏫", layout="centered")

# --- CUSTOM CSS FOR BETTER UI ---
st.markdown("""
    <style>
    .main-header { font-size: 36px; font-weight: bold; color: #1E3A8A; text-align: center; }
    .sub-header { font-size: 18px; color: #4B5563; text-align: center; margin-bottom: 30px; }
    .stApp { background-color: #f8fafc; }
    </style>
    """, unsafe_allow_html=True)

# --- BACKEND INITIALIZATION ---
@st.cache_resource
def init_rag_system():
    # Fetch key from .env
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("❌ API Key not found in .env file!")
        st.stop()

    # Load local vector database
    embeddings = get_embedding_model()
    vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Setup LLM (Groq)
    llm = ChatGroq(api_key=api_key, model_name=GROQ_MODEL, temperature=0)

    # Define the System Instructions
    system_prompt = (
        "You are the official School AI Assistant. "
        "Use the provided context to answer questions accurately and politely. "
        "If the answer is not in the context, say you don't know."
        "\n\nContext: {context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    # Build the RAG Chain
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, combine_docs_chain)

# Initialize the system
try:
    rag_chain = init_rag_system()
except Exception as e:
    st.error(f"Failed to load system: {e}")
    st.stop()

# --- MAIN UI ---
st.markdown('<p class="main-header">🏫 School AI Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your 24/7 Guide for Syllabus, Exams & Holidays</p>', unsafe_allow_html=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your school assistant. How can I help you today?"}
    ]

# Display Chat History
for message in st.session_state.messages:
    avatar = "👨‍🎓" if message["role"] == "user" else "🏫"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# User Input Logic
if user_query := st.chat_input("Ask me about the curriculum..."):
    
    # --- 1. GUARDRAIL: INPUT CHECK ---
    is_safe, security_msg = check_input_safety(user_query)
    
    if not is_safe:
        with st.chat_message("assistant", avatar="🛡️"):
            st.error(security_msg)
    else:
        # Show user message
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user", avatar="👨‍🎓"):
            st.markdown(user_query)

        # Generate AI Response
        with st.chat_message("assistant", avatar="🏫"):
            with st.spinner("Searching school records..."):
                try:
                    response = rag_chain.invoke({"input": user_query})
                    answer = response["answer"]
                    
                    # --- 2. GUARDRAIL: OUTPUT CHECK ---
                    final_answer = check_output_safety(answer)
                    
                    st.markdown(final_answer)
                    st.session_state.messages.append({"role": "assistant", "content": final_answer})
                except Exception as e:
                    st.error(f"Error generating response: {e}")

# Sidebar Info
with st.sidebar:
    st.title("Settings")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.info("This assistant uses RAG technology to provide factual school data.")