import os
import pandas as pd
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from src.config import DB_DIR
from src.embedder import get_embedding_model
from ragas import evaluate
# Updated for RAGAS 0.4.x Collections
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from datasets import Dataset

load_dotenv()

# --- 1. SETUP THE RAG SYSTEM FOR TESTING ---
def get_eval_chain():
    # Load your existing local embeddings
    embed_model = get_embedding_model()
    
    vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embed_model)
    
    # Using Llama 3.3 70B for high-quality evaluation
    eval_llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")
    
    return vectorstore, eval_llm, embed_model

# --- 2. DEFINE TEST DATASET ---
test_questions = [
    {
        "question": "When is the Hindi exam for SA1?",
        "ground_truth": "The Hindi exam for SA1 is scheduled for August 8, 2025."
    },
    {
        "question": "What is the syllabus for Mathematics Number Systems?",
        "ground_truth": "The syllabus for Mathematics Number Systems includes Real Numbers."
    },
    {
        "question": "When do the Dussehra holidays start?",
        "ground_truth": "The Dussehra holidays start on October 16, 2025, and end on October 23, 2025."
    }
]

def run_evaluation():
    # Now returning embed_model too
    vectorstore, llm, embed_model = get_eval_chain() 
    results = []
    
    print(f"--- Starting Evaluation on {len(test_questions)} questions ---")
    
    for item in test_questions:
        # A. Retrieval
        docs = vectorstore.similarity_search(item['question'], k=3)
        contexts = [doc.page_content for doc in docs]
        
        # B. Generation
        full_prompt = f"Context: {' '.join(contexts)}\nQuestion: {item['question']}"
        response = llm.invoke(full_prompt)
        
        results.append({
            "user_input": item['question'],
            "answer": response.content,
            "retrieved_contexts": contexts,
            "ground_truth": item['ground_truth']
        })

    # --- 3. RUN RAGAS METRICS ---
    dataset = Dataset.from_list(results)
    
    print("Calculating RAGAS scores (Using Groq LLM + Local Embeddings)...")
    
    # IMPORTANT: We explicitly pass 'embeddings=embed_model' so it doesn't ask for OpenAI
    score = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision],
        llm=llm,
        embeddings=embed_model 
    )
    
    # --- 4. DISPLAY RESULTS ---
    df = score.to_pandas()
    print("\n--- EVALUATION REPORT ---")
    print(df[['user_input', 'faithfulness', 'answer_relevancy', 'context_precision']])
    
    df.to_csv("evaluation_report.csv", index=False)
    print("\n✅ Report saved to evaluation_report.csv")

if __name__ == "__main__":
    run_evaluation()