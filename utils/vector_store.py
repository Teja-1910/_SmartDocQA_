import chromadb
import uuid

# create persistent DB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="documents")


def store_embeddings(chunks, embeddings, company):
    # delete old data of same company
    existing = collection.get(where={"company": company})

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    ids = [str(uuid.uuid4()) for _ in chunks]

    metadata = [{"company": company} for _ in chunks]

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids,
        metadatas=metadata
    )


def query_embeddings(query_embedding, company, k=5):
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=k,
        where={"company": company}
    )

    docs = results["documents"]

    if not docs or not docs[0]:
        return []

    return docs[0]