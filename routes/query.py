from fastapi import APIRouter
from pydantic import BaseModel
from utils.embeddings import get_embeddings
from utils.vector_store import query_embeddings
from utils.llm import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    question: str
    company: str


@router.post("/ask")
def ask_question(request: QueryRequest):
    
    if not request.company:
        return {"answer": "Please provide company name"}

    if not request.question:
        return {"answer": "Please provide a question"}

    query_embedding = get_embeddings([request.question])
    
    docs = query_embeddings(query_embedding, request.company)

    if not docs:
       return {"answer": "Sorry, No data found for this company"}

    context = "\n\n".join(docs)

    answer = generate_answer(context, request.question)

    return {
    "company": request.company,
    "question": request.question,
    "answer": answer
}