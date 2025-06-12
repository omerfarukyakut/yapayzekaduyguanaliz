import pandas as pd
from textblob import TextBlob

class AfitapDetection:
    def __init__(self, data):
        self.data = data

    def analyze_sentiment(self):
        self.data['sentiment'] = self.data['content'].apply(self.get_sentiment)
        return self.data

    def get_sentiment(self, text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    def detect_misleading_info(self):
        misleading_keywords = ['yanıltıcı', 'sahte', 'kandırıcı']
        self.data['misleading'] = self.data['content'].apply(lambda x: any(keyword in x for keyword in misleading_keywords))
        return self.data

    def detect_competitor_comparisons(self):
        competitor_keywords = ['rakip', 'karşılaştırma', 'üstün']
        self.data['competitor_comparison'] = self.data['content'].apply(lambda x: any(keyword in x for keyword in competitor_keywords))
        return self.data

    def run_analysis(self):
        self.analyze_sentiment()
        self.detect_misleading_info()
        self.detect_competitor_comparisons()
        return self.data

# Example usage:
# data = pd.DataFrame({'content': ['Afitap Meyhane harika!', 'Bu meyhane sahte bilgiler veriyor.']})
# afitap_detector = AfitapDetection(data)
# results = afitap_detector.run_analysis()
# print(results)