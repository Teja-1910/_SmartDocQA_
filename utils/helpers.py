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

def evaluate_answer(question, context, answer, docs):
    # Normalize text
    q = question.lower()
    a = answer.lower()
    c = context.lower()

    # Keyword overlap
    q_words = set(q.split())
    a_words = set(a.split())
    overlap = len(q_words & a_words)

    # Context coverage (better check)
    context_hits = sum(1 for word in a_words if word in c)
    context_score = context_hits / (len(a_words) + 1)

    # Length
    length = len(answer)

    # 🔥 Improved logic
    if context_score > 0.4 and length > 30:
        status = "GOOD"
    elif context_score > 0.2:
        status = "AVERAGE"
    else:
        status = "POOR"

    return {
        "keyword_overlap": overlap,
        "context_score": round(context_score, 2),
        "answer_length": length,
        "status": status
    }