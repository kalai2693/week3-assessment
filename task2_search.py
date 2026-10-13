import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Twelve FAQ questions (4 HR, 4 IT, 4 Payroll)
faqs = [
    # HR
    "What is the work from home policy?",
    "How many days of annual leave do I get?",
    "How do I apply for maternity or paternity leave?",
    "What is the dress code in the office?",
    # IT
    "How do I reset my password?",
    "How do I connect to the company VPN?",
    "My laptop is slow, who should I contact?",
    "How do I request new software installation?",
    # Payroll
    "What date are salaries paid every month?",
    "How do I download my payslip?",
    "How do I update my bank account details for salary?",
    "How is income tax deducted from my pay?",
]

# 2. Convert FAQs to embeddings (numbers that represent meaning)
model = SentenceTransformer("all-MiniLM-L6-v2")
faq_embeddings = model.encode(faqs)


# 3. Cosine similarity written by ourselves with numpy
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# 4. Semantic search: find FAQs closest in meaning
def semantic_search(query, top_k=3):
    query_embedding = model.encode(query)
    scores = [cosine_similarity(query_embedding, e) for e in faq_embeddings]
    best = np.argsort(scores)[::-1][:top_k]
    return [(faqs[i], round(float(scores[i]), 2)) for i in best]


# 5. Keyword search: find FAQs sharing the same words
def keyword_search(query):
    query_words = set(query.lower().split())
    results = []
    for faq in faqs:
        faq_words = set(faq.lower().replace("?", "").split())
        common = query_words & faq_words
        if common:
            results.append((faq, len(common)))
    results.sort(key=lambda x: x[1], reverse=True)
    return results


# 6. Test the 3 queries
queries = ["I cannot log in", "when is salary credited", "work from home rules"]

for q in queries:
    print("=" * 60)
    print("QUERY:", q)
    print("\nKeyword search:")
    kw = keyword_search(q)
    if kw:
        for faq, count in kw[:3]:
            print("  -", faq, f"(shared words: {count})")
    else:
        print("  No results")
    print("\nSemantic search:")
    for faq, score in semantic_search(q):
        print("  -", faq, f"(score: {score})")