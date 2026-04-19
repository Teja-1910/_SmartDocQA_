from fastapi import APIRouter, UploadFile, File

from utils.pdf_loader import load_pdf
from utils.chunking import chunk_text
from utils.embeddings import get_embeddings
from utils.vector_store import store_embeddings
from utils.helpers import extract_company_from_filename

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()

        company = extract_company_from_filename(file.filename)
        company = company.lower().strip()   

        print("UPLOAD COMPANY:", company)

        text = load_pdf(file_bytes)

        if not text.strip():
            return {"error": "No text extracted"}

        chunks = chunk_text(text, 500, 100)

        embeddings = get_embeddings(chunks)

        store_embeddings(chunks, embeddings, company)

        return {
            "message": "Upload successful",
            "company": company,
            "chunks": len(chunks)
        }

    except Exception as e:
        print("❌ UPLOAD ERROR:", e)
        return {"error": str(e)}