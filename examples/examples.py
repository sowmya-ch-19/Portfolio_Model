# examples/example_usage.py

from code.sentiment_analysis import analyze_sentiment

# Example texts
texts = [
    "I love this product, it's amazing!",
    "This is a bad experience.",
    "It's okay, nothing special."
]

# Analyze sentiment for each text
for text in texts:
    sentiment = analyze_sentiment(text)
    print(f"Text: {text} -> Sentiment: {sentiment}")
