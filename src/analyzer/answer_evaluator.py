import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os
import re

# ================= LOAD =================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'qa_dataset.csv')

df = pd.read_csv(DATA_PATH)

model = SentenceTransformer('all-MiniLM-L6-v2')

# ================= PRECOMPUTE =================
questions = df['question'].tolist()
question_embeddings = model.encode(questions)

# ================= HELPER =================
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text

# ================= FIND MATCH =================
def find_best_match(question):
    query_embedding = model.encode([question])
    similarities = cosine_similarity(query_embedding, question_embeddings)[0]
    best_idx = similarities.argmax()
    return df.iloc[best_idx]['answer']

# ================= KEYWORD SCORING =================
def keyword_score(expected, user):
    expected_words = set(clean_text(expected).split())
    user_words = set(clean_text(user).split())

    common = expected_words.intersection(user_words)

    if len(expected_words) == 0:
        return 0

    return len(common) / len(expected_words)

# ================= LENGTH CHECK =================
def length_score(answer):
    words = len(answer.split())

    if words > 80:
        return 1
    elif words > 40:
        return 0.8
    elif words > 20:
        return 0.6
    else:
        return 0.3

# ================= AI DETECTION =================
def detect_ai_generated(answer):
    text = answer.lower()

    generic_phrases = [
        "in conclusion",
        "in today's world",
        "it is important to note",
        "this highlights that",
        "overall",
        "in summary",
        "as we know",
        "it plays a crucial role",
        "widely used",
        "various applications"
    ]

    generic_score = sum(1 for p in generic_phrases if p in text)

    # 🔹 Repetition check
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    repetition = 0
    for i in range(len(sentences) - 1):
        if sentences[i] == sentences[i+1]:
            repetition += 1

    # 🔹 Vocabulary diversity
    words = text.split()
    unique_ratio = len(set(words)) / (len(words) + 1)

    length = len(words)

    # 🔥 AI SCORE
    ai_score = 0

    if generic_score >= 2:
        ai_score += 0.4
    if repetition > 0:
        ai_score += 0.2
    if unique_ratio < 0.5:
        ai_score += 0.2
    if length > 120:
        ai_score += 0.2

    # 🔥 LABEL
    if ai_score > 0.6:
        label = "⚠️ Likely AI-generated"
    elif ai_score > 0.4:
        label = "🤔 Possibly AI-generated"
    else:
        label = "✅ Likely human-written"

    return label, ai_score

# ================= EVALUATE =================
def evaluate_answer(question, user_answer):

    expected = find_best_match(question)

    # 🔹 Semantic
    emb_expected = model.encode([expected])
    emb_user = model.encode([user_answer])
    semantic = cosine_similarity(emb_expected, emb_user)[0][0]

    # 🔹 Keyword
    keyword = keyword_score(expected, user_answer)

    # 🔹 Length
    length = length_score(user_answer)

    # 🔥 FINAL SCORE
    final_score = (
        (semantic * 0.5) +
        (keyword * 0.3) +
        (length * 0.2)
    )

    score = int(final_score * 10)

    # 🔥 FEEDBACK
    if final_score > 0.75:
        feedback = "Excellent answer"
    elif final_score > 0.55:
        feedback = "Good answer"
    elif final_score > 0.35:
        feedback = "Average answer"
    else:
        feedback = "Weak answer"

    # 🔹 AI DETECTION
    ai_label, ai_score = detect_ai_generated(user_answer)

    # 🔥 FINAL OUTPUT
    feedback += f"\nSemantic: {semantic:.2f}, Keyword: {keyword:.2f}, Length: {length:.2f}"
    feedback += f"\nAI Detection: {ai_label} (score: {ai_score:.2f})"

    return score, feedback