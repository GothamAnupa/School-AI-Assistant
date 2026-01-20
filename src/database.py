from langchain_chroma import Chroma

def save_to_vector_db(chunks, embeddings, db_path):
    print(f"--- Creating Vector DB at {db_path} ---")
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_path
    )
    print("--- Database Saved Successfully ---")
    return vector_db