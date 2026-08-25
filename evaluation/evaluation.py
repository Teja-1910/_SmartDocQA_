import os
import csv
import numpy as np
import matplotlib.pyplot as plt

from utils.embeddings import get_embeddings
from utils.vector_store import query_embeddings
from utils.llm import generate_answer


COMPANY = "hyniva"

TEST_CASES = [
    {
        "question": "What dress code do employees need to maintain?",
        "expected": "Employees must follow the formal dress code."
    },
    {
        "question": "What are the working hours?",
        "expected": "Employees must follow the prescribed working hours."
    },
    {
        "question": "What is the leave policy?",
        "expected": "Employees are entitled to leave according to company policy."
    }
]


def cosine_similarity(a, b):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)


def get_embedding(text):
    return get_embeddings([text])[0]


def evaluate_retrieval(question_embedding, expected, retrieved_docs):
    expected_embedding = get_embedding(expected)

    best_score = 0.0

    for doc in retrieved_docs:
        doc_embedding = get_embedding(doc)

        score = cosine_similarity(
            expected_embedding,
            doc_embedding
        )

        best_score = max(best_score, score)

    hit = best_score >= 0.60

    return hit, best_score


def evaluate_relevance(question, answer):
    question_embedding = get_embedding(question)
    answer_embedding = get_embedding(answer)

    return cosine_similarity(
        question_embedding,
        answer_embedding
    )


def evaluate_correctness(expected, answer):
    expected_embedding = get_embedding(expected)
    answer_embedding = get_embedding(answer)

    return cosine_similarity(
        expected_embedding,
        answer_embedding
    )


def evaluate_faithfulness(answer, context):
    answer_embedding = get_embedding(answer)

    context_chunks = context.split("\n")

    if not context_chunks:
        return 0.0

    scores = []

    for chunk in context_chunks:

        if not chunk.strip():
            continue

        chunk_embedding = get_embedding(chunk)

        score = cosine_similarity(
            answer_embedding,
            chunk_embedding
        )

        scores.append(score)

    if not scores:
        return 0.0

    return max(scores)


def save_csv(results):
    os.makedirs("evaluation_results", exist_ok=True)

    file_path = "evaluation_results/evaluation_results.csv"

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "question",
                "expected",
                "generated",
                "retrieval_hit",
                "retrieval_score",
                "relevance",
                "correctness",
                "faithfulness",
                "overall"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to: {file_path}")


def create_metric_chart(
    retrieval_rate,
    relevance,
    correctness,
    faithfulness
):

    os.makedirs("evaluation_results", exist_ok=True)

    metrics = [
        "Retrieval Hit Rate",
        "Answer Relevance",
        "Answer Correctness",
        "Faithfulness"
    ]

    scores = [
        retrieval_rate * 100,
        relevance * 100,
        correctness * 100,
        faithfulness * 100
    ]

    plt.figure(figsize=(10, 6))

    bars = plt.bar(metrics, scores)

    plt.title("SmartDocQA RAG Evaluation")
    plt.ylabel("Score (%)")
    plt.ylim(0, 100)

    for bar, score in zip(bars, scores):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{score:.1f}%",
            ha="center"
        )

    plt.xticks(rotation=15)
    plt.tight_layout()

    plt.savefig(
        "evaluation_results/metric_evaluation.png",
        dpi=300
    )

    plt.close()

    print(
        "Metric chart saved to: "
        "evaluation_results/metric_evaluation.png"
    )


def create_question_chart(results):

    os.makedirs("evaluation_results", exist_ok=True)

    questions = [
        f"Q{i + 1}"
        for i in range(len(results))
    ]

    scores = [
        result["overall"] * 100
        for result in results
    ]

    plt.figure(figsize=(10, 6))

    bars = plt.bar(questions, scores)

    plt.title("SmartDocQA Question-wise Performance")
    plt.xlabel("Questions")
    plt.ylabel("Overall Score (%)")
    plt.ylim(0, 100)

    for bar, score in zip(bars, scores):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{score:.1f}%",
            ha="center"
        )

    plt.tight_layout()

    plt.savefig(
        "evaluation_results/question_performance.png",
        dpi=300
    )

    plt.close()

    print(
        "Question chart saved to: "
        "evaluation_results/question_performance.png"
    )


def evaluate():

    results = []

    retrieval_hits = 0
    relevance_scores = []
    correctness_scores = []
    faithfulness_scores = []

    print("\n")
    print("=" * 70)
    print("                 SMARTDOCQA EVALUATION")
    print("=" * 70)

    for i, test in enumerate(TEST_CASES, 1):

        question = test["question"]
        expected = test["expected"]

        print("\n")
        print(f"QUESTION {i}")
        print("-" * 70)

        print("Question:")
        print(question)

        query_embedding = get_embedding(question)

        retrieved_docs = query_embeddings(
            query_embedding,
            COMPANY,
            k=5
        )

        if not retrieved_docs:

            print("\nNo documents retrieved.")

            result = {
                "question": question,
                "expected": expected,
                "generated": "No answer",
                "retrieval_hit": False,
                "retrieval_score": 0.0,
                "relevance": 0.0,
                "correctness": 0.0,
                "faithfulness": 0.0,
                "overall": 0.0
            }

            results.append(result)

            continue

        context = "\n".join(retrieved_docs)

        answer = generate_answer(
            context,
            question
        )

        retrieval_hit, retrieval_score = evaluate_retrieval(
            query_embedding,
            expected,
            retrieved_docs
        )

        relevance = evaluate_relevance(
            question,
            answer
        )

        correctness = evaluate_correctness(
            expected,
            answer
        )

        faithfulness = evaluate_faithfulness(
            answer,
            context
        )

        overall = (
            retrieval_hit
            + relevance
            + correctness
            + faithfulness
        ) / 4

        if retrieval_hit:
            retrieval_hits += 1

        relevance_scores.append(relevance)
        correctness_scores.append(correctness)
        faithfulness_scores.append(faithfulness)

        print("\nExpected Answer:")
        print(expected)

        print("\nGenerated Answer:")
        print(answer)

        print("\nMetrics:")
        print(
            f"Retrieval Hit:      "
            f"{'PASS' if retrieval_hit else 'FAIL'} "
            f"({retrieval_score:.2f})"
        )

        print(
            f"Answer Relevance:   "
            f"{relevance * 100:.2f}%"
        )

        print(
            f"Answer Correctness: "
            f"{correctness * 100:.2f}%"
        )

        print(
            f"Faithfulness:       "
            f"{faithfulness * 100:.2f}%"
        )

        print(
            f"Question Score:     "
            f"{overall * 100:.2f}%"
        )

        results.append({
            "question": question,
            "expected": expected,
            "generated": answer,
            "retrieval_hit": retrieval_hit,
            "retrieval_score": retrieval_score,
            "relevance": relevance,
            "correctness": correctness,
            "faithfulness": faithfulness,
            "overall": overall
        })

    total = len(TEST_CASES)

    retrieval_rate = retrieval_hits / total

    avg_relevance = (
        np.mean(relevance_scores)
        if relevance_scores
        else 0.0
    )

    avg_correctness = (
        np.mean(correctness_scores)
        if correctness_scores
        else 0.0
    )

    avg_faithfulness = (
        np.mean(faithfulness_scores)
        if faithfulness_scores
        else 0.0
    )

    overall_score = (
        retrieval_rate
        + avg_relevance
        + avg_correctness
        + avg_faithfulness
    ) / 4

    print("\n")
    print("=" * 70)
    print("                    FINAL RESULTS")
    print("=" * 70)

    print(f"Total Questions:       {total}")
    print(
        f"Retrieval Hit Rate:    "
        f"{retrieval_rate * 100:.2f}%"
    )
    print(
        f"Average Relevance:     "
        f"{avg_relevance * 100:.2f}%"
    )
    print(
        f"Average Correctness:   "
        f"{avg_correctness * 100:.2f}%"
    )
    print(
        f"Average Faithfulness:  "
        f"{avg_faithfulness * 100:.2f}%"
    )
    print(
        f"Overall Score:         "
        f"{overall_score * 100:.2f}%"
    )

    print("=" * 70)

    save_csv(results)

    create_metric_chart(
        retrieval_rate,
        avg_relevance,
        avg_correctness,
        avg_faithfulness
    )

    create_question_chart(results)


if __name__ == "__main__":
    evaluate()