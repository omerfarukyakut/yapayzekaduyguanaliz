import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class MisleadingDetection:
    def __init__(self, data):
        self.data = data
        self.model = None

    def preprocess_data(self):
        self.data['label'] = self.data['label'].map({'misleading': 1, 'not_misleading': 0})
        return self.data

    def train_model(self):
        X = self.data['text']
        y = self.data['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = make_pipeline(CountVectorizer(), MultinomialNB())
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        print(classification_report(y_test, predictions))

    def predict(self, new_data):
        if self.model is None:
            raise Exception("Model has not been trained yet.")
        return self.model.predict(new_data)

    def analyze_misleading_content(self):
        misleading_content = self.data[self.data['label'] == 1]
        return misleading_content[['text', 'label']]