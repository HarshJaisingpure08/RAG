from pypdf import PdfReader
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def readPDF():
    pdf = PdfReader(r"C:\Users\harsh\OneDrive\Desktop\RAG\simple_python.pdf")
    output = []

    for page_no, page in enumerate(pdf.pages):
        output.append({
            "page_no": page_no,
            "page_content": page.extract_text()
        })

    return output


pdf_context = readPDF()

SYSTEM_PROMPT = f"""
You are an AI expert Assistant specialized in Python programming.
Your job is to answer user queries using ONLY the information available in the provided "context".

If a user asks a question NOT related to the context, respond with:
"I am sorry, I can only assist with queries related to the provided context."

---
### Context
{pdf_context}
---

### Rules
1. Use only the provided context.
2. Keep answers concise and professional.
3. Include the page number if the answer is found.
4. If information is missing, respond politely.
5. Do not hallucinate or use external knowledge.
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

while True:
    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    assistant_reply = response.choices[0].message.content
    print("Assistant:", assistant_reply)

    messages.append({"role": "assistant", "content": assistant_reply})
