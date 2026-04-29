import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.generator import generate_questions
from src.analyzer import evaluate_answer, extract_skills, load_skills
from src.parser import extract_text

# ================= PAGE CONFIG =================
st.set_page_config(page_title="AI Interview System", layout="wide")

# ================= CUSTOM CSS =================
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
h1 {
    text-align: center;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 15px;
}
.skill-box {
    background-color: #262730;
    padding: 8px;
    border-radius: 6px;
    margin: 4px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("<h1>🎯 AI Interview Preparation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Smart Resume-Based Interview Practice</p>", unsafe_allow_html=True)

# ================= SESSION =================
if "questions" not in st.session_state:
    st.session_state.questions = []

# ================= UPLOAD =================
st.markdown("### 📄 Upload Resume")

uploaded_file = st.file_uploader("", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)

    skills_list = load_skills()
    skills = extract_skills(text, skills_list)

    # ================= SKILLS =================
    st.markdown("### 🧠 Detected Skills")
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if skills:
        for skill in skills:
            st.markdown(f'<span class="skill-box">{skill}</span>', unsafe_allow_html=True)
    else:
        st.warning("No skills detected")

    st.markdown('</div>', unsafe_allow_html=True)

    # ================= GENERATE =================
    if st.button("🚀 Generate Questions"):
        st.session_state.questions = generate_questions(skills)

# ================= QUESTIONS =================
if st.session_state.questions:
    st.markdown("### 💬 Interview Questions")

    answers = []

    for i, q in enumerate(st.session_state.questions):
        st.markdown(f'<div class="card"><b>Q{i+1}:</b> {q}</div>', unsafe_allow_html=True)
        ans = st.text_area("Your Answer", key=f"ans_{i}")
        answers.append(ans)

    # ================= EVALUATE =================
    if st.button("📊 Evaluate Answers"):

        if any(ans.strip() == "" for ans in answers):
            st.error("⚠️ Please answer all questions")
        else:
            st.markdown("### 📊 Results")

            total_score = 0

            for i, ans in enumerate(answers):
                q = st.session_state.questions[i]

                score, feedback = evaluate_answer(q, ans)
                total_score += score

                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.write(f"**Q{i+1} Score:** {score}/10")
                st.write(f"**Feedback:** {feedback}")
                st.markdown('</div>', unsafe_allow_html=True)

            # ================= FINAL SCORE =================
            avg_score = total_score / len(answers)

            st.markdown("### 🏆 Final Performance")

            col1, col2, col3 = st.columns(3)

            col2.metric("Average Score", f"{avg_score:.2f}/10")

            st.progress(avg_score / 10)

            if avg_score > 7:
                st.success("Excellent performance! 🎉")
            elif avg_score > 5:
                st.warning("Good, but can improve")
            else:
                st.error("Needs improvement")