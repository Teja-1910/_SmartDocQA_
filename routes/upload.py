from fastapi import APIRouter, UploadFile, File, HTTPException

from utils.pdf_loader import load_pdf
from utils.chunking import chunk_text
from utils.embeddings import get_embeddings
from utils.vector_store import store_embeddings
from utils.helpers import extract_company_from_filename

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # 1. Read uploaded PDF
        file_bytes = await file.read()

        # 2. Extract company name from filename
        company = extract_company_from_filename(file.filename)
        company = company.lower().strip()

        print("UPLOAD COMPANY:", company)

        # 3. Extract text from PDF
        documents = load_pdf(file_bytes)

        if not documents:
            raise HTTPException(
                status_code=400,
                detail="No text extracted from the PDF"
            )

        # 4. Chunk the extracted text
        chunks = chunk_text(documents, 500, 100)

        if not chunks:
            raise HTTPException(
                status_code=400,
                detail="No chunks created from the document"
            )

        # 5. Make sure embeddings receive ONLY text
        text_chunks = []

        for chunk in chunks:

            if isinstance(chunk, dict):

                # If chunk contains "text"
                if "text" in chunk:
                    text_chunks.append(chunk["text"])

                # Fallback if another text field is used
                elif "content" in chunk:
                    text_chunks.append(chunk["content"])

                else:
                    print("WARNING: Unknown chunk format:", chunk)

            elif isinstance(chunk, str):
                text_chunks.append(chunk)

        if not text_chunks:
            raise HTTPException(
                status_code=400,
                detail="No valid text chunks available for embedding"
            )

        print("NUMBER OF CHUNKS:", len(text_chunks))
        print("FIRST CHUNK:", text_chunks[0])
        print("CHUNK TYPE:", type(text_chunks[0]))

        # 6. Generate embeddings
        embeddings = get_embeddings(text_chunks)

        print("EMBEDDING TYPE:", type(embeddings))
        print("FIRST EMBEDDING TYPE:", type(embeddings[0]))

        # 7. Store chunks + embeddings in vector database
        store_embeddings(
            text_chunks,
            embeddings,
            company
        )

        # 8. Return successful response
        return {
            "message": "Upload successful",
            "company": company,
            "chunks": len(text_chunks),
            "pages": len(documents)
        }

    except HTTPException:
        raise

    except Exception as e:
        print("UPLOAD ERROR:", e)

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    