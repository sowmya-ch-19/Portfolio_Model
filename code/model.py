# your_model.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

class SentimentAnalyzer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(tokenizer=self.tokenize, stop_words='english')
        self.clf = make_pipeline(StandardScaler(with_mean=False), SVC(kernel='linear'))

    def tokenize(self, text):
        tokens = word_tokenize(text)
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return tokens

    def train(self, X_train, y_train):
        X_train_vectorized = self.vectorizer.fit_transform(X_train)
        self.clf.fit(X_train_vectorized, y_train)

    def predict(self, X_test):
        X_test_vectorized = self.vectorizer.transform(X_test)
        return self.clf.predict(X_test_vectorized)
