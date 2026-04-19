import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")


def generate_answer(context, question):
    try:
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
            },
            timeout=30
        )

        print("STATUS:", response.status_code)
        print("FULL RESPONSE:", response.text)

        if response.status_code != 200:
            return "LLM server error"

        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"].strip()
        else:
            return "Error generating answer"

    except Exception as e:
        print(" LLM ERROR:", e)
        return "Error generating answer"