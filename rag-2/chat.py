from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

user_input = input("User >> ")

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="genai",
    embedding=embeddings
)

documents = vector_db.similarity_search(query=user_input)

def build_context():
    data = []
    for doc in documents:
        data.append({
            "page_no": doc.metadata.get("page_label"),
            "page_content": doc.page_content
        })
    return data

system_prompt = f"""
You are an AI assistant that answers questions strictly using the provided context.

---
Context:
{build_context()}
---

Rules:
1. Use only the given context.
2. Mention the page number if the answer exists.
3. If the answer is not found, reply politely that the information is unavailable.
4. Do not generate external knowledge.
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_input}
]

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

print("🤖", response.choices[0].message.content)
