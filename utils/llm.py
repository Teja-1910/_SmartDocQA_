import requests
import os

API_KEY = os.getenv("GROQ-API-KEY")

def generate_answer(context, question):

    prompt = f"""
You are a strict document assistant.

Rules:
- Answer ONLY from the context
- If answer not found, say: "Answer not found in document"
- Do NOT guess
- Keep answer short

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    print("STATUS:", response.status_code)
    print("FULL RESPONSE:", response.text)

    data = response.json()

    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        return f"LLM ERROR: {data}"