from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    # Chunk text for long inputs
    max_chunk = 1000
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]

    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
        summaries.append(summary[0]["summary_text"])

    return "\n".join(summaries)
