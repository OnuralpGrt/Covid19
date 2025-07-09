# COVID-19 Veri Analiz Web Uygulaması

Bu uygulama, COVID-19 ile ilgili farklı veri setlerinden elde edilen analizleri ve görselleri modern bir web arayüzünde sunar. Uygulama Streamlit ile geliştirilmiştir.

## Özellikler
- En çok vaka ve ölüm görülen ülkeler tablosu
- Kıta bazında özet tablo
- Günlük ve haftalık analiz grafiklerinin görselleri
- ABD county bazında özet grafik
- Tüm analiz görsellerinin kolayca görüntülenmesi
- Kullanılan tüm CSV veri setlerini tek tıkla indirme butonu

## Klasör Yapısı

```
Covid19/
├── analiz_ciktisi/         # Otomatik üretilen analiz görselleri ve tabloları
├── webapp/
│   ├── app.py              # Streamlit web uygulaması ana dosyası
│   └── README.md           # (Bu dosya)
├── worldometer_data.csv    # Veri setleri
├── country_wise_latest.csv
├── day_wise.csv
├── full_grouped.csv
├── usa_county_wise.csv
├── covid_19_clean_complete.csv
└── covid19_analysis.py     # Analiz ve görsel üretim scripti
```

## Kurulum ve Çalıştırma

1. **Gerekli kütüphaneleri yükleyin:**

```bash
pip install streamlit pillow pandas
```

2. **Analiz ve görselleri oluşturun:**

Ana dizinde aşağıdaki komutu çalıştırarak analiz_ciktisi klasöründe tüm görsellerin ve tabloların oluşmasını sağlayın:

```bash
python3 covid19_analysis.py
```

3. **Web arayüzünü başlatın:**

webapp klasörüne girip Streamlit uygulamasını başlatın:

```bash
cd webapp
streamlit run app.py
```

4. **Tarayıcıdan uygulamaya erişin:**

Aşağıdaki adreslerden birini tarayıcınızda açın:
- http://localhost:8501
- veya terminalde gösterilen Network URL

## Notlar
- Web arayüzünde en altta bulunan buton ile kullanılan tüm CSV veri setlerini tek bir zip dosyası olarak indirebilirsiniz.
- Görseller ve tablolar otomatik olarak analiz_ciktisi klasöründe üretilir.
- Uygulama tamamen yerel olarak çalışır, verileriniz dışarıya gönderilmez.

---
Herhangi bir sorun veya geliştirme öneriniz olursa iletebilirsiniz. 