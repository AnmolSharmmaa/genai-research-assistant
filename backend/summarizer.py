from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    text = text.strip().replace("\n", " ")

    max_chunk_len = 1000  
    words = text.split()
    chunks = [' '.join(words[i:i+max_chunk_len]) for i in range(0, len(words), max_chunk_len)]

    summary_parts = []
    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=60, do_sample=False)
        summary_parts.append(result[0]["summary_text"])

    full_summary = ' '.join(summary_parts)

    words = full_summary.split()
    if len(words) > 150:
        full_summary = ' '.join(words[:150]) + '...'

    return full_summary

