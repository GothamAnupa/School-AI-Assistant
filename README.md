# 🏫 Narayana School RAG Assistant

A modular Retrieval-Augmented Generation (RAG) chatbot designed to answer student queries about syllabus, exams, and academic calendars for Narayana Public School.

## 🚀 Tech Stack
- **Framework:** LangChain
- **LLM:** Groq (Llama 3.1)
- **Embeddings:** HuggingFace (all-MiniLM-L6-v2)
- **Vector Store:** ChromaDB
- **UI:** Streamlit

## 📂 Project Structure
- `ingest_main.py`: Modular pipeline for data parsing, chunking, and embedding.
- `app.py`: Streamlit chat interface with session management.
- `src/`: Core logic for the RAG pipeline.
- `data/`: Source documents in text format.

## 🛠️ Setup Instructions
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file with your `GROQ_API_KEY`.
4. Run ingestion: `python ingest_main.py`.
5. Start the bot: `streamlit run app.py`.