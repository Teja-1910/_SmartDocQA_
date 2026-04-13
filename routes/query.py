from fastapi import APIRouter
from pydantic import BaseModel

from utils.embeddings import get_embeddings
from utils.vector_store import query_embeddings
from utils.llm import generate_answer
from utils.helpers import extract_company_from_email

router = APIRouter()


class QueryRequest(BaseModel):
    question: str
    user_email: str


@router.post("/ask")
def ask_question(request: QueryRequest):
    try:
        company = extract_company_from_email(request.user_email)
        company = company.lower().strip()   # 🔥 FIX

        print("QUERY COMPANY:", company)

        query_embedding = get_embeddings([request.question])[0]

        docs = query_embeddings(query_embedding, company)

        if not docs:
            return {"answer": "No data found for your company"}

        context = " ".join(docs)[:1500]

        answer = generate_answer(context, request.question)

        return {"answer": answer}

    except Exception as e:
        print("❌ QUERY ERROR:", e)
        return {"answer": "Error generating answer"}