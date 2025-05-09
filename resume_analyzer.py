import ollama
import os

# Utilisation correcte de l'API Ollama pour appeler le modèle
def analyze_resume(resume_text, job_description=None):
    prompt = f"""
You are an experienced HR professional with technical expertise.
Your task is to review the following resume and give an objective evaluation.

Instructions:
- Mention if the profile matches jobs like Data Scientist, DevOps, ML Engineer, etc.
- List strengths and weaknesses.
- Suggest skills and online courses for improvement.

Resume:
{resume_text}
"""
    if job_description:
        prompt += f"\n\nJob Description:\n{job_description}\n\nCompare this resume to the job and highlight strengths/weaknesses accordingly."

    # Envoyer la requête à l'API Ollama avec le modèle approprié
    response = ollama.chat(model="llama3:latest", messages=[{"role": "user", "content": prompt}])
    
    return response['message']['content'].strip()

