from langchain_huggingface import HuggingFaceEmbeddings
from src.config import EMBED_MODEL

def get_embedding_model():
    print(f"--- Initializing Embedder: {EMBED_MODEL} ---")
    return HuggingFaceEmbeddings(model_name=EMBED_MODEL)