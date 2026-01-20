from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(documents):
    print("--- Splitting into chunks ---")
    # 1000 chars with 150 overlap for context retention
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    return splitter.split_documents(documents)