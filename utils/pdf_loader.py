import PyPDF2
import io

def load_pdf(file_bytes):
    reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    
    documents = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        documents.append({
        "text": text,
        "page": i + 1
    })

    return documents