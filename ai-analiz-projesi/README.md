# AI Analiz Projesi

Bu proje, sosyal medya ve diğer platformlarda yer alan yanıltıcı bilgi, karalama, rakip markalarla haksız karşılaştırma ve "Afitap Meyhane" ile ilgili paylaşımları analiz etmek için geliştirilmiş bir yapay zeka uygulamasıdır. Proje, duygu analizi ve çeşitli analiz yöntemleri kullanarak bu tür içerikleri tespit etmeyi amaçlamaktadır.

## Proje Yapısı

- **src/app.py**: Uygulamanın giriş noktasıdır. Veri yükleme, model eğitimi ve analiz işlemlerini başlatan ana işlevleri içerir.
- **src/data/data_loader.py**: Verilerin yüklenmesi ve ön işlenmesi için gerekli işlevleri içerir. Veritabanından veya dosyalardan veri çekme işlemlerini gerçekleştirir.
- **src/models/sentiment_model.py**: Duygu analizi için kullanılan yapay zeka modelini tanımlar. Modelin eğitimi ve tahmin işlemleri için gerekli sınıfları ve işlevleri içerir.
- **src/analysis/misleading_detection.py**: Yanıltıcı bilgi ve karalama içeriklerini tespit etmek için gerekli algoritmaları ve işlevleri içerir.
- **src/analysis/competitor_analysis.py**: Rakip markalarla haksız karşılaştırma ve örtülü reklamları analiz eden işlevleri içerir.
- **src/analysis/afitap_detection.py**: "Afitap Meyhane" ile ilgili paylaşımları analiz eden ve özellik arz eden içerikleri tespit eden işlevleri içerir.
- **src/utils/helpers.py**: Projede kullanılan yardımcı işlevleri ve genel amaçlı araçları içerir.
- **src/types/index.py**: Projede kullanılan veri tiplerini ve arayüzleri tanımlar.
- **requirements.txt**: Projede kullanılan Python kütüphanelerinin listesini içerir ve gerekli bağımlılıkları belirtir.

## Kurulum

Projenin çalışabilmesi için gerekli bağımlılıkları yüklemek için aşağıdaki komutu kullanabilirsiniz:

```
pip install -r requirements.txt
```

## Kullanım

Projenin çalıştırılması için `src/app.py` dosyasını çalıştırmanız yeterlidir. Bu dosya, veri yükleme, model eğitimi ve analiz işlemlerini başlatacaktır.

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request oluşturun veya sorunlarınızı bildirin.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.