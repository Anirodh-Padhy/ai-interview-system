# 🎯 AI Interview Preparation System

### 🚀 Smart Resume-Based Interview Practice using AI & NLP

---

## 📌 Overview

The **AI Interview Preparation System** is an intelligent web application that helps users prepare for technical interviews by analyzing their resume, generating relevant questions, and evaluating answers using advanced NLP techniques.

It combines **semantic similarity, keyword analysis, and AI-style detection** to provide realistic interview feedback.

---

## 🧠 Key Features

* 📄 **Resume Upload & Parsing**

  * Extracts text from PDF resumes
  * Handles real-world resume formats

* 🧠 **Smart Skill Extraction (NLP)**

  * Uses spaCy for skill detection
  * Supports synonyms (e.g., ML → Machine Learning)

* 🎯 **Dynamic Question Generation**

  * Generates questions based on detected skills
  * Fallback system for general questions

* 📊 **Hybrid Answer Evaluation**

  * Semantic similarity (Sentence Transformers)
  * Keyword matching
  * Answer length analysis

* 🤖 **AI Answer Detection**

  * Detects generic / AI-like responses
  * Uses linguistic patterns and heuristics

* 📈 **Performance Dashboard**

  * Question-wise scoring
  * Final performance score
  * Visual feedback

---

## 🧰 Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **NLP:** spaCy
* **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
* **ML Tools:** scikit-learn
* **Data Handling:** Pandas
* **PDF Parsing:** PyPDF2 / pdfplumber

---

## 📁 Project Structure

```
ai-interview-system/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   │   ├── train.csv
│   │   └── valid.csv
│   └── processed/
│       └── qa_dataset.csv
│
├── scripts/
│   └── clean_dataset.py
│
├── src/
│   ├── analyzer/
│   │   ├── answer_evaluator.py
│   │   └── skill_extractor.py
│   │
│   ├── generator/
│   │   └── question_generator.py
│   │
│   └── parser/
│       └── resume_parser.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/ai-interview-system.git
cd ai-interview-system
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```

streamlit run app/streamlit_app.py
```

---

## 📊 How It Works

1. Upload your resume (PDF)
2. System extracts skills using NLP
3. Generates interview questions
4. User answers questions
5. AI evaluates answers using:

   * Semantic similarity
   * Keyword overlap
   * Answer quality
6. Provides score + feedback + AI detection

---

## 🎯 Sample Output

* 📊 Score: 7/10
* 💬 Feedback: Good answer, can improve clarity
* 🤖 AI Detection: Possibly AI-generated
* 📈 Final Performance Score with visualization

---

## ⚠️ Limitations

* AI detection is heuristic-based (not 100% accurate)
* PDF parsing may struggle with scanned resumes
* Dataset quality affects evaluation accuracy

---

## 🚀 Future Improvements

* 🔥 LLM-based evaluation (OpenAI / Gemini)
* 📱 Mobile-friendly UI
* 🎙️ Voice-based interview simulation
* 🧠 Advanced skill extraction using embeddings
* 📊 Analytics dashboard (history tracking)

---

## 💡 Key Learnings

* NLP-based skill extraction
* Semantic similarity using embeddings
* Hybrid evaluation system design
* Real-world data preprocessing
* Building end-to-end AI applications

---

## 👨‍💻 Author

**Anirodh Padhy**

* 💼 Aspiring AI/ML Engineer
* 💻 GitHub: (www.linkedin.com/in/anirodh-padhy-ab3455315)
* 🔗 LinkedIn: (https://github.com/Anirodh-Padhy)

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
