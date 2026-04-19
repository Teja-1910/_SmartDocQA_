from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

def get_embeddings(texts):
    return model.encode(texts).tolist()
