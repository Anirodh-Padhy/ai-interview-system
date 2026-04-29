import PyPDF2
import re

def extract_text(uploaded_file):
    text = ""

    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:   # ✅ prevent None issue
                text += page_text + " "

    except Exception as e:
        return ""

    # 🔥 CLEAN TEXT
    text = text.lower()

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()