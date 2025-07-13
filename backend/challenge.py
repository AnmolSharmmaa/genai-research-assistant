import random
import re

def generate_questions(context):
    # Split into sentences
    sentences = re.split(r'(?<=[.!?]) +', context.strip())
    questions = []

    # Shuffle for randomness
    random.shuffle(sentences)

    # Generate real logic/comprehension-based questions
    for sentence in sentences:
        words = sentence.split()
        if len(words) >= 8:
            if " is " in sentence:
                parts = sentence.split(" is ", 1)
                noun_phrase = parts[0].strip().split()[-1]
                question = f"What is {noun_phrase}?"
                answer = parts[1].strip().rstrip(".")
                justification = sentence
            elif " because " in sentence:
                parts = sentence.split(" because ", 1)
                question = f"Why {parts[0].strip().rstrip('.')}?"
                answer = parts[1].strip().rstrip(".")
                justification = sentence
            else:
                continue

            questions.append({
                "question": question,
                "answer": answer,
                "justification": justification
            })

            if len(questions) >= 3:
                break

    # If not enough valid questions, use varied fallbacks
    fallback_questions = [
        {
            "question": "What is the central idea of the document?",
            "answer": "AI research and its impact",
            "justification": "The overall content revolves around artificial intelligence and its applications."
        },
        {
            "question": "Which major technology does the document emphasize?",
            "answer": "Machine Learning",
            "justification": "Machine Learning is discussed as a foundational component."
        },
        {
            "question": "Why is data important in the document?",
            "answer": "It enables better decision-making.",
            "justification": "The text emphasizes how data supports intelligent systems and efficiency."
        },
        {
            "question": "What does automation help with?",
            "answer": "Increases efficiency and reduces human effort.",
            "justification": "Automation is described as improving workflows and reducing manual work."
        }
    ]

    random.shuffle(fallback_questions)

    # Add fallback if needed
    if len(questions) < 3:
        questions += fallback_questions[:3 - len(questions)]

    return questions
def evaluate_answer(user_answer, correct_answer):
    # Simple relaxed comparison
    user = user_answer.lower().strip()
    correct = correct_answer.lower().strip()

    if correct in user or user in correct:
        return True, "✅ Well done! Your answer seems correct."
    else:
        return False, f"❌ Expected something like: {correct_answer}"
