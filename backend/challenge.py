# backend/challenge.py
import random
import re

def generate_questions(text):
    sentences = re.split(r'(?<=[.?!])\s+', text)
    questions = []
    for _ in range(3):
        sent = random.choice(sentences).strip()
        question = f"What is the main idea of: \"{sent}\"?"
        answer = sent
        questions.append({"question": question, "answer": answer})
    return questions

def evaluate_answer(user_answer, correct_answer):
    user = user_answer.lower().strip()
    correct = correct_answer.lower().strip()
    if correct in user or user in correct:
        return True, "✅ Correct!"
    else:
        return False, f"❌ Expected something like: {correct_answer}"
