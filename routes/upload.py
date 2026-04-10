from fastapi import APIRouter, UploadFile, File
from utils.chunking import chunk_text
from utils.embeddings import get_embeddings
from utils.vector_store import store_embeddings
from utils.pdf_loader import load_pdf

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    company = file.filename.split(".")[0]

    contents = await file.read()

    text = load_pdf(contents)

    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)

    store_embeddings(chunks, embeddings, company)

    return {
        "message": f"{company} uploaded successfully"
    }