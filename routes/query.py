from fastapi import APIRouter
from pydantic import BaseModel
from utils.embeddings import get_embeddings
from utils.vector_store import query_embeddings
from utils.llm import generate_answer
from utils.helpers import evaluate_answer

router = APIRouter()


class QueryRequest(BaseModel):
    question: str
    company: str


@router.post("/query")
def ask_question(request: QueryRequest):
    try:

        company = request.company.lower().strip()

        print("\n" + "=" * 60)
        print("SMARTDOCQA LIVE QUERY")
        print("=" * 60)
        print("COMPANY:", company)
        print("QUESTION:", request.question)

        query_embedding = get_embeddings([request.question])[0]

        docs = query_embeddings(
            query_embedding,
            company,
            k=5
        )

        if not docs:
            print("NO DOCUMENTS FOUND")
            return {
                "answer": "No data found for your company"
            }

        context = " ".join(docs)[:1500]

        answer = generate_answer(
            context,
            request.question
        )

        evaluation = evaluate_answer(
            request.question,
            context,
            answer,
            docs
        )

        print("=" * 60)

        return {
            "answer": answer,
            "evaluation": evaluation
        }

    except Exception as e:
        print("❌ QUERY ERROR:", e)

        return {
            "answer": "Error generating answer"
        }