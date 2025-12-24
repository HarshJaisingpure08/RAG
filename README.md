FOR rag-2 only

```md
# PDF Question Answering System (RAG)

This project is a simple question-answering system built on top of a PDF file.  
Users can ask questions, and the system returns answers based only on the content of the PDF.

---

## Overview

The project uses a Retrieval-Augmented Generation (RAG) approach.

First, the PDF is processed and stored in a vector database.  
Later, when a user asks a question, the most relevant parts of the PDF are retrieved and used to generate the answer.

If the answer does not exist in the document, the system clearly states that the information is not available.

---

## How the system works

1. The PDF file is loaded and split into smaller text chunks  
2. Each chunk is converted into a vector embedding  
3. All embeddings are stored in a Qdrant vector database  
4. The user enters a question  
5. The question is converted into an embedding  
6. Similar text chunks are retrieved from the database  
7. The language model generates an answer using only the retrieved text  

---

## Project structure

```

.
├── chat.py          # Handles user queries and answers
├── ingestion.py     # Processes and stores the PDF data
├── python.pdf       # Source document
├── .env             # API key configuration
├── README.md

````

---

## Technologies used

- Python
- LangChain
- OpenAI API
- Qdrant
- Docker

---

## Setup instructions

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Start the vector database

Run Qdrant using Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

## Ingest the PDF

Run this command once to store the PDF data:

```bash
python ingestion.py
```

---

## Ask questions

Start the application:

```bash
python chat.py
```

Enter your question in the terminal.
If the answer exists in the PDF, it will be returned.
If not, the system will respond that the information is unavailable.

---

## Notes

* `ingestion.py` must be run before `chat.py`
* Answers are generated only from the PDF content
* No external knowledge is used
