from transformers import pipeline  
# pipeline lets us use pretrained models easily

# Load a model that already knows summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Send text to model and ask for a short version
    result = summarizer(text, max_length=120, min_length=30, do_sample=False)
    
    # Model gives a list, so take first result
    return result[0]["summary_text"]
