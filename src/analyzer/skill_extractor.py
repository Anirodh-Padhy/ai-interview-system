import spacy
from spacy.matcher import PhraseMatcher

# ================= LOAD =================
nlp = spacy.load("en_core_web_sm")

# 🔥 Skill synonyms
SKILL_SYNONYMS = {
    "machine learning": ["ml", "machine learning"],
    "deep learning": ["dl", "deep learning"],
    "python": ["python"],
    "data science": ["data science", "data analysis"],
    "sql": ["sql", "mysql", "postgres"],
    "java": ["java"],
    "c++": ["c++", "cpp"]
}

# ================= BUILD MATCHER (ONCE) =================
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

all_patterns = []

for skill, synonyms in SKILL_SYNONYMS.items():
    for phrase in synonyms:
        all_patterns.append(nlp(phrase))

matcher.add("SKILLS", all_patterns)


# ================= LOAD SKILLS =================
def load_skills():
    return list(SKILL_SYNONYMS.keys())


# ================= EXTRACT SKILLS =================
def extract_skills(text, skills_list):
    doc = nlp(text)

    matches = matcher(doc)

    found_skills = set()

    for match_id, start, end in matches:
        span = doc[start:end].text.lower()

        # 🔥 Map synonym → main skill
        for skill, synonyms in SKILL_SYNONYMS.items():
            if span in synonyms:
                found_skills.add(skill)

    return sorted(list(found_skills))