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
   ```bash
   pip install -r requirements.txt
