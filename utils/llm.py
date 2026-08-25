import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")


def generate_answer(context, question):
    try:
        prompt = f"""
You are SmartDocQA, a strict company document assistant.

Your job is to answer the user's question using ONLY the provided context.

IMPORTANT RULES:
- Give the shortest possible answer that completely answers the question.
- Prefer ONE short sentence whenever possible.
- Do not explain extra details unless they are specifically asked for.
- Do not repeat the question.
- Do not provide unnecessary background information.
- Do not add examples unless the question asks for examples.
- Do not guess or use outside knowledge.
- If the answer is not clearly available in the context, say exactly:
  "Answer not found in the document."
- If the context contains a direct answer, return only that answer.
- Keep responses precise, direct, and easy to understand.

Example:
Question: "What dress code do I need to maintain?"
Good answer: "Employees must follow the prescribed formal dress code."
Bad answer: A long explanation of the company's entire dress-code policy.

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
                "model": "openai/gpt-oss-20b",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 512
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

        return "Error generating answer"

    except Exception as e:
        print("LLM ERROR:", e)
        return "Error generating answer"