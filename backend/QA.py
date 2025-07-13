import streamlit as st
from openai import OpenAI
import re

# Initialize GROQ OpenAI-compatible client
client = OpenAI(
    api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

def answer_question(question, context):
    # Prompt for LLaMA 3
    prompt = f"""
You are a helpful academic assistant. Use the document provided below to answer the user's question.

📄 Document:
\"\"\"
{context}
\"\"\"

❓ Question:
{question}

💬 Answer:
"""

    # Call GROQ API (LLaMA 3 - 70B)
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a research assistant that only uses the uploaded document to answer questions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=800
    )

    # Extract answer
    answer = response.choices[0].message.content.strip()

    # Optional: Try to find a sentence in the context that contains part of the answer
    sentences = re.split(r'(?<=[.!?]) +', context)
    justification = next((s for s in sentences if answer[:20] in s), "Based on the document content.")

    return answer, justification
