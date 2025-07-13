from transformers import pipeline
import re
QA_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")


def answer_question(question, context):
    result = QA_model(question=question, context=context[:1024])
    answer = result["answer"]

    sentences = re.split(r'(?<=[.!?]) +', context)
    justification = next((s for s in sentences if answer in s), "No exact sentence found.")

    return answer, justification
