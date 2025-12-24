from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("python.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=500
)

chunks = splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

QdrantVectorStore.from_documents(
    url="http://localhost:6333",
    collection_name="genai",
    embedding=embeddings,
    documents=chunks
)

print("Ingestion completed")
