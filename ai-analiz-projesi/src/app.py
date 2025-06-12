from data.data_loader import load_data
from models.sentiment_model import SentimentModel
from analysis.misleading_detection import detect_misleading_content
from analysis.competitor_analysis import analyze_competitors
from analysis.afitap_detection import detect_afitap_content

def main():
    # Veri yükleme
    data = load_data()

    # Duygu analizi modeli oluşturma ve eğitme
    model = SentimentModel()
    model.train(data)

    # Yanıltıcı içeriklerin tespiti
    misleading_results = detect_misleading_content(data)

    # Rakip analizleri
    competitor_results = analyze_competitors(data)

    # Afitap Meyhane içeriklerinin analizi
    afitap_results = detect_afitap_content(data)

    # Sonuçları yazdırma
    print("Yanıltıcı İçerik Sonuçları:", misleading_results)
    print("Rakip Analiz Sonuçları:", competitor_results)
    print("Afitap Meyhane İçerik Sonuçları:", afitap_results)

if __name__ == "__main__":
    main()