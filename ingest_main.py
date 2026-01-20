from src.config import DATA_PATH, DB_DIR
from src.loader import get_documents
from src.splitter import split_text
from src.embedder import get_embedding_model
from src.database import save_to_vector_db

def run_pipeline():
    # Execute the steps
    docs = get_documents(DATA_PATH)
    chunks = split_text(docs)
    embed_model = get_embedding_model()
    save_to_vector_db(chunks, embed_model, DB_DIR)
    
    print("\n✅ DATA INGESTION COMPLETE")

if __name__ == "__main__":
    run_pipeline()