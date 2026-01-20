from langchain_community.document_loaders import TextLoader

def get_documents(file_path):
    print(f"--- Loading: {file_path} ---")
    loader = TextLoader(file_path, encoding="utf-8")
    return loader.load()