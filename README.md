# AI Resume Analyzer (Local & Privacy-Preserving)

This project is a **local AI-powered resume analyzer** built with [Ollama](https://ollama.com) and [Streamlit](https://streamlit.io).
Unlike cloud-based tools, **your resume data never leaves your machine**, making it ideal for users who care about privacy.

Whether you're a **freelancer** improving your resume,  **a student** / **a job seeker tailoring your profile to a job offer**, or an **HR professional reviewing CVs offline**, this tool helps you analyze and enhance resumes **securely and efficiently**; all **without an internet connection** and **without uploading your documents to untrusted or shady websites**.

## ✅ Why Local?

Most resume analyzers send your data to external servers. This tool:

* **Runs entirely on your computer**
* **Uses local Large Language Models (LLMs)** via Ollama
* **Keeps your personal documents secure and private**

---

## Features

* Upload your resume (PDF or image)
* Optionally paste a job description
* Analyze strengths, weaknesses, and skill gaps
* Get personalized recommendations (courses, tools, etc.)
* All processing is **offline** – no internet needed after setup

## 🛠️ Tech Stack

* Python 3.10+
* Streamlit (for UI)
* Ollama (to run local LLMs like `llama3` or `mistral`)
* pdfplumber, pytesseract, Pillow

---

## 🔐 Security & Privacy

> Your resume is never uploaded or shared — everything happens locally on your device.

* Ideal for HR, freelancers, or job seekers who handle sensitive data
* No external API calls
* No cloud storage

---

## Installation

1. **Clone the repo**
2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # For Windows
   source venv/bin/activate  # For macOS/Linux
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Install Ollama and Pull a Model**
   Download from: [https://ollama.com](https://ollama.com)
   In terminal:

   ```bash
       ollama pull llama3
   ```
5. **▶️ Run the App**

   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```markdown
AI_Resume_Analyzer_Ollama
├── app.py                  # Streamlit UI
├── resume_analyzer.py      # Core logic using Ollama
├── utils.py                # Text extraction
└── requirements.txt
```
## ❗ Notes
Make sure your PC has at least 6GB of free RAM for llama3. Try mistral if you need a lighter model.

For image-based resumes, ensure Tesseract OCR is installed and added to your system PATH.


## 📄 License
This project is open-source and free to use for educational or personal projects.



Made by Ijja – because privacy matters.

```
