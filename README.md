# AI Document Assistant

An AI-powered RAG application that allows users to ask factual questions and extract insights from documents and websites.

## Purpose

Built to help anyone quickly find answers, summarize content, and extract key information from:
* Personal or professional notes, documentation, and reference materials
* Reports, data sheets, and official announcements
* Project guidelines, schedules, and compliance documents
* Public websites, blogs, and online documentation

## Features

* **Multi-Format Support:** Upload `.txt`, `.md`, `.log`, `.csv`, `.pdf`, and `.docx` files
* **Web Scraping:** Paste website links and query their content directly
* **Conversational Chat:** Ask follow-up questions with full chat history
* **Source Citations:** Get accurate answers backed by clear references to the source material
* **Dynamic Knowledge Base:** Reset or rebuild the indexed content anytime

## How It Works

1. **Ingestion:** Upload files or paste website links.
2. **Processing:** The app extracts the text and splits it into manageable chunks.
3. **Indexing:** Chunks are converted into embeddings and stored in a vector database.
4. **Retrieval:** Your questions are matched against the indexed content to find relevant context.
5. **Generation:** The model generates an answer using only the retrieved information to prevent hallucinations.

## Project Structure

* `app.py` - Streamlit UI and chat workflow
* `src/knowledge.py` - Document loading, web scraping, chunking, and retrieval logic
* `src/guardrails.py` - Input/output safety and validation checks
* `src/config.py` - Model configurations and storage settings

## Run Locally

1. Install dependencies:
  
   pip install -r requirements.txt
   
2.Create a .env file and set your API key:
  GROQ_API_KEY=your_api_key_here
  
3.Launch the application:
 streamlit run app.py

𝗨𝘀𝗮𝗴𝗲
1.Add your documents or links in the sidebar.
2.Click Build knowledge base.
3.Type your question in the chat box and interact with your data.

𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝 𝐒𝐨𝐮𝐫𝐜𝐞𝐬
1.Local documents: .txt, .md, .log, .csv, .pdf, .docx

2.Web pages: Text content extracted from pasted URLs

𝐍𝐨𝐭𝐞𝐬
1.The application answers questions strictly based on the indexed sources.

2.Streamlit Cloud uses a disabled file watcher configuration to optimize performance and reduce background warnings.
