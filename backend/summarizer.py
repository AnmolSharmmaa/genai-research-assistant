
import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

def summarize_text(text):
    prompt = f"Summarize the following academic or research text:\n\n{text}\n\nSummary:"

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful research summarizer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=800
    )

    return response.choices[0].message.content.strip()
