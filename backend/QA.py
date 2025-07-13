# backend/QA.py

from transformers import pipeline
import re

# Load the Q&A pipeline with DistilBERT
QA_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question, context):
    # Trim context to first 1024 characters for performance (can increase if needed)
    result = QA_model(question=question, context=context[:1024])
    answer = result["answer"]

    # Try to find a sentence in the context that contains the answer
    sentences = re.split(r'(?<=[.!?]) +', context)
    justification = next((s for s in sentences if answer in s), "No exact sentence found.")

    return answer, justification
