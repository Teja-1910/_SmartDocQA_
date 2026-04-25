def chunk_text(documents, chunk_size=500, overlap=100):
    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk_size")

    if not documents:
        return []

    chunks = []

    for doc in documents:
        text = doc.get("text", "")
        page = doc.get("page", None)

        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            if chunk.strip():
                chunks.append({
                    "text": chunk,
                    "page": page   # 🔥 keep page info
                })

            start = end - overlap

    return chunks