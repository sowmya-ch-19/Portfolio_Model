from your_model import SentimentAnalyzer

# Example usage
texts = [
    "I love this product, it's amazing!",
    "This is a bad experience.",
    "It's okay, nothing special."
]
labels = ['positive', 'negative', 'neutral']

X_train = texts
y_train = labels

analyzer = SentimentAnalyzer()
analyzer.train(X_train, y_train)

X_test = ["I am extremely happy with the service.", "The food was terrible and the service was bad."]
predicted_labels = analyzer.predict(X_test)

print(predicted_labels)
