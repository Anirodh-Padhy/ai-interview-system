import json
import random

# ================= LOAD =================
def load_questions():
    with open("data/questions.json") as f:
        return json.load(f)


# ================= GENERATE =================
def generate_questions(skills, num_questions=5):
    question_bank = load_questions()
    questions = []

    # 🔥 deterministic randomness (optional but good)
    random.seed(42)

    # 🔹 Collect questions based on skills
    for skill in skills:
        if skill in question_bank:
            skill_questions = question_bank[skill]

            questions.extend(
                random.sample(
                    skill_questions,
                    min(2, len(skill_questions))
                )
            )

    # 🔥 Remove duplicates
    questions = list(set(questions))

    # 🔥 Fallback if no questions found
    if not questions:
        all_questions = []
        for qs in question_bank.values():
            all_questions.extend(qs)

        questions = random.sample(
            all_questions,
            min(num_questions, len(all_questions))
        )

    # 🔥 Final selection
    return questions[:num_questions]