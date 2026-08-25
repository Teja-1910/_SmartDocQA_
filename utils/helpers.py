import numpy as np
from utils.embeddings import get_embeddings


def extract_company_from_email(email: str):
    try:
        return email.split("@")[1].split(".")[0].lower().strip()
    except:
        return "unknown"


def extract_company_from_filename(filename: str):
    try:
        name = filename.lower().strip()
        name = name.split(".")[0]
        name = name.replace("-", "_")
        company = name.split("_")[0]
        return company
    except:
        return "unknown"


def cosine_similarity(a, b):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)


def evaluate_answer(question, context, answer, docs):

    question_embedding = get_embeddings([question])[0]
    answer_embedding = get_embeddings([answer])[0]

    relevance = cosine_similarity(
        question_embedding,
        answer_embedding
    )

    retrieval_scores = []

    for doc in docs:
        doc_embedding = get_embeddings([doc])[0]

        score = cosine_similarity(
            question_embedding,
            doc_embedding
        )

        retrieval_scores.append(score)

    retrieval_relevance = (
        max(retrieval_scores)
        if retrieval_scores
        else 0.0
    )

    faithfulness_scores = []

    for doc in docs:
        doc_embedding = get_embeddings([doc])[0]

        score = cosine_similarity(
            answer_embedding,
            doc_embedding
        )

        faithfulness_scores.append(score)

    faithfulness = (
        max(faithfulness_scores)
        if faithfulness_scores
        else 0.0
    )

    overall_score = (
        retrieval_relevance
        + relevance
        + faithfulness
    ) / 3

    print("\n" + "=" * 60)
    print("SMARTDOCQA LIVE EVALUATION")
    print("=" * 60)

    print("\nQuestion:")
    print(question)

    print("\nGenerated Answer:")
    print(answer)

    print(f"\nRetrieved Chunks: {len(docs)}")

    print(
        f"Retrieval Relevance: {retrieval_relevance * 100:.2f}%"
    )

    print(
        f"Answer Relevance:    {relevance * 100:.2f}%"
    )

    print(
        f"Faithfulness:        {faithfulness * 100:.2f}%"
    )

    print(
        f"Overall Score:       {overall_score * 100:.2f}%"
    )

    print("=" * 60)

    return {
        "retrieval_relevance": round(retrieval_relevance, 4),
        "answer_relevance": round(relevance, 4),
        "faithfulness": round(faithfulness, 4),
        "overall_score": round(overall_score, 4),
        "retrieved_chunks": len(docs)
    }