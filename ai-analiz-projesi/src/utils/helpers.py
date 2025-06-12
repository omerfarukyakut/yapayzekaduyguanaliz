def load_data(file_path):
    # Veriyi belirtilen dosya yolundan yükler
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_text(text):
    # Metni ön işleme tabi tutar
    import re
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    return text

def calculate_sentiment_score(predictions):
    # Duygu analizi sonuçlarının puanını hesaplar
    return sum(predictions) / len(predictions) if predictions else 0

def extract_keywords(text, num_keywords=5):
    # Metinden anahtar kelimeleri çıkarır
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(stop_words='english', max_features=num_keywords)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()