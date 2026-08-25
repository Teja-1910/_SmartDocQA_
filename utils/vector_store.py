import os
import uuid
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index("smartdocqa")


def store_embeddings(chunks, embeddings, company):
    try:
        company = company.lower().strip()

        vectors = []

        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

            if isinstance(chunk, dict):
                if "text" in chunk:
                    text = chunk["text"]
                elif "content" in chunk:
                    text = chunk["content"]
                else:
                    continue
            else:
                text = str(chunk)

            vectors.append({
                "id": f"{company}_{i}_{uuid.uuid4().hex[:8]}",
                "values": embedding,
                "metadata": {
                    "text": text,
                    "company": company
                }
            })

        if not vectors:
            raise ValueError("No valid vectors created")

        response = index.upsert(
            vectors=vectors,
            namespace=company
        )

        print(f"Stored {len(vectors)} chunks in Pinecone namespace: {company}")
        print("Pinecone response:", response)

        return True

    except Exception as e:
        print("STORE ERROR:", e)
        raise


def query_embeddings(query_embedding, company, k=5):
    try:
        company = company.lower().strip()

        results = index.query(
            vector=query_embedding,
            top_k=k,
            include_metadata=True,
            namespace=company
        )

        matches = results.get("matches", [])

        docs = [
            match["metadata"]["text"]
            for match in matches
            if "metadata" in match
            and "text" in match["metadata"]
        ]

        print(f"Retrieved {len(docs)} docs from Pinecone namespace: {company}")

        return docs

    except Exception as e:
        print("QUERY ERROR:", e)
        raise