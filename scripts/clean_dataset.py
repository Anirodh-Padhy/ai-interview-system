import pandas as pd
import re

# ================= LOAD =================
train = pd.read_csv("data/train.csv")
valid = pd.read_csv("data/valid.csv")

# Combine
df = pd.concat([train, valid], ignore_index=True)

print("Columns found:", df.columns)

# ================= SELECT =================
df = df[['Title', 'Body']]

df = df.rename(columns={
    'Title': 'question',
    'Body': 'answer'
})

# ================= CLEAN TEXT =================
def clean_text(text):
    text = str(text)

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Remove code snippets
    text = re.sub(r'`.*?`', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

df['question'] = df['question'].apply(clean_text)
df['answer'] = df['answer'].apply(clean_text)

# ================= FILTER =================
df = df.dropna()
df = df.drop_duplicates()

# Remove too short answers
df = df[df['answer'].str.split().str.len() > 10]

# Remove too long answers (optional)
df = df[df['answer'].str.split().str.len() < 300]

# ================= SAMPLE =================
sample_size = min(500, len(df))
df = df.sample(sample_size, random_state=42)

# ================= SAVE =================
df.to_csv("data/qa_dataset.csv", index=False)

print(f"✅ Dataset cleaned successfully! Rows: {len(df)}")