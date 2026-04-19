from fastapi import APIRouter
from pydantic import BaseModel
from utils.embeddings import get_embeddings
from utils.vector_store import query_embeddings
from utils.llm import generate_answer
from utils.helpers import evaluate_answer

router = APIRouter()


# ✅ UPDATED MODEL (NO EMAIL)
class QueryRequest(BaseModel):
    question: str
    company: str


@router.post("/query")
def ask_question(request: QueryRequest):
    try:
        # 🔥 USE COMPANY DIRECTLY (NO EMAIL)
        company = request.company.upper().strip()

        print("QUERY COMPANY:", company)

        # 🔥 EMBEDDING
        query_embedding = get_embeddings([request.question])[0]

        # 🔥 PINECONE SEARCH
        docs = query_embeddings(query_embedding, company)

        if not docs:
            return {"answer": "No data found for your company"}

        # 🔥 CONTEXT
        context = " ".join(docs)[:1500]

        # 🔥 LLM
        answer = generate_answer(context, request.question)
        evaluation = evaluate_answer(request.question, context, answer, docs)
        return {
        "answer": answer,
        "evaluation": evaluation
       }


    except Exception as e:
        print("❌ QUERY ERROR:", e)
        return {"answer": "Error generating answer"}