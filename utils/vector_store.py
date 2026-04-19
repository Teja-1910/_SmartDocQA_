import os
import uuid
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("smartdocqa")


def store_embeddings(chunks, embeddings, company):
    try:
        company = company.lower().strip()   

        vectors = []

        for chunk, embedding in zip(chunks, embeddings):
            vectors.append({
                "id": str(uuid.uuid4()),
                "values": embedding,
                "metadata": {
                    "text": chunk
                }
            })

        index.upsert(
            vectors=vectors,
            namespace=company 
        )

        print(f"Stored {len(vectors)} chunks in {company}")

    except Exception as e:
        print("STORE ERROR:", e)


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
            if "metadata" in match and "text" in match["metadata"]
        ]

        print(f" Retrieved {len(docs)} docs from {company}")

        return docs

    except Exception as e:
        print(" QUERY ERROR:", e)
        return []