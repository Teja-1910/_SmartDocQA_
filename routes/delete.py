from fastapi import APIRouter
from pydantic import BaseModel
from utils.vector_store import index  # your pinecone index

router = APIRouter()


class DeleteRequest(BaseModel):
    company: str


@router.post("/delete")
def delete_company_data(request: DeleteRequest):
    try:
        company = request.company.strip().upper()

        print("DELETING COMPANY:", company)

        # 🔥 DELETE ALL DATA FROM PINECONE
        index.delete(delete_all=True, namespace=company)

        return {"message": "Deleted successfully"}

    except Exception as e:
        print("❌ DELETE ERROR:", e)
        return {"message": "Delete failed"}