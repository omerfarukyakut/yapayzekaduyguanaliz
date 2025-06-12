from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
import pandas as pd

class SentimentModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = RandomForestClassifier()

    def train(self, data, labels):
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
        X_train_vectorized = self.vectorizer.fit_transform(X_train)
        self.model.fit(X_train_vectorized, y_train)
        X_test_vectorized = self.vectorizer.transform(X_test)
        predictions = self.model.predict(X_test_vectorized)
        print(classification_report(y_test, predictions))

    def predict(self, new_data):
        new_data_vectorized = self.vectorizer.transform(new_data)
        return self.model.predict(new_data_vectorized)