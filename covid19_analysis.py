import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Grafiklerin Türkçe karakter desteği için
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

# CSV dosya yolları
WORLDOMETER_PATH = 'worldometer_data.csv'
COUNTRY_LATEST_PATH = 'country_wise_latest.csv'
DAY_WISE_PATH = 'day_wise.csv'
FULL_GROUPED_PATH = 'full_grouped.csv'
USA_COUNTY_PATH = 'usa_county_wise.csv'
CLEAN_COMPLETE_PATH = 'covid_19_clean_complete.csv'

# Klasör oluştur (çıktılar için)
os.makedirs('analiz_ciktisi', exist_ok=True)

def oku_worldometer():
    return pd.read_csv(WORLDOMETER_PATH)

def oku_country_latest():
    return pd.read_csv(COUNTRY_LATEST_PATH)

def oku_day_wise():
    return pd.read_csv(DAY_WISE_PATH)

def oku_full_grouped():
    return pd.read_csv(FULL_GROUPED_PATH)

def oku_usa_county():
    return pd.read_csv(USA_COUNTY_PATH)

def oku_clean_complete():
    return pd.read_csv(CLEAN_COMPLETE_PATH)

# Devamında her dosya için analiz fonksiyonları ve grafikler eklenecek... 

def analiz_worldometer():
    df = oku_worldometer()
    # Eksik verileri doldur
    df = df.fillna(0)
    
    # En çok vaka görülen ilk 10 ülke
    top_cases = df.sort_values('TotalCases', ascending=False).head(10)
    top_cases[['Country/Region', 'TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases']].to_csv('analiz_ciktisi/worldometer_top_cases.csv', index=False)
    
    # En çok ölüm görülen ilk 10 ülke
    top_deaths = df.sort_values('TotalDeaths', ascending=False).head(10)
    top_deaths[['Country/Region', 'TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases']].to_csv('analiz_ciktisi/worldometer_top_deaths.csv', index=False)
    
    # Kıta bazında toplam vaka ve ölüm
    continent_summary = df.groupby('Continent').agg({'TotalCases':'sum', 'TotalDeaths':'sum', 'TotalRecovered':'sum', 'ActiveCases':'sum'}).reset_index()
    continent_summary.to_csv('analiz_ciktisi/worldometer_continent_summary.csv', index=False)
    
    # Ölüm oranı, iyileşme oranı, aktif vaka oranı
    df['Olum_Orani'] = (df['TotalDeaths'] / df['TotalCases']) * 100
    df['Iyilesme_Orani'] = (df['TotalRecovered'] / df['TotalCases']) * 100
    df['Aktif_Oran'] = (df['ActiveCases'] / df['TotalCases']) * 100
    oranlar = df[['Country/Region', 'Olum_Orani', 'Iyilesme_Orani', 'Aktif_Oran']].sort_values('Olum_Orani', ascending=False)
    oranlar.to_csv('analiz_ciktisi/worldometer_oranlar.csv', index=False)
    
    # Grafik: En çok vaka görülen 10 ülke
    plt.figure(figsize=(12,6))
    sns.barplot(x='TotalCases', y='Country/Region', data=top_cases, palette='Reds_r')
    plt.title('En Çok Vaka Görülen 10 Ülke')
    plt.xlabel('Toplam Vaka')
    plt.ylabel('Ülke')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/worldometer_top_cases.png')
    plt.close()
    
    # Grafik: En çok ölüm görülen 10 ülke
    plt.figure(figsize=(12,6))
    sns.barplot(x='TotalDeaths', y='Country/Region', data=top_deaths, palette='Blues_r')
    plt.title('En Çok Ölüm Görülen 10 Ülke')
    plt.xlabel('Toplam Ölüm')
    plt.ylabel('Ülke')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/worldometer_top_deaths.png')
    plt.close()
    
    # Grafik: Kıta bazında toplam vaka
    plt.figure(figsize=(10,5))
    sns.barplot(x='TotalCases', y='Continent', data=continent_summary, palette='viridis')
    plt.title('Kıta Bazında Toplam Vaka')
    plt.xlabel('Toplam Vaka')
    plt.ylabel('Kıta')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/worldometer_continent_cases.png')
    plt.close()
    
    # Grafik: Kıta bazında toplam ölüm
    plt.figure(figsize=(10,5))
    sns.barplot(x='TotalDeaths', y='Continent', data=continent_summary, palette='magma')
    plt.title('Kıta Bazında Toplam Ölüm')
    plt.xlabel('Toplam Ölüm')
    plt.ylabel('Kıta')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/worldometer_continent_deaths.png')
    plt.close()
    
    print('worldometer_data.csv analizleri tamamlandı. Sonuçlar analiz_ciktisi klasöründe.')

def death_rate_by_country():
    df = oku_worldometer()
    df = df.fillna(0)
    df = df[df['TotalCases'] > 0]  # Sıfır vaka olanları çıkar
    df['Olum_Orani'] = (df['TotalDeaths'] / df['TotalCases']) * 100
    oran_tablosu = df[['Country/Region', 'TotalCases', 'TotalDeaths', 'Olum_Orani']].sort_values('Olum_Orani', ascending=False)
    oran_tablosu.to_csv('analiz_ciktisi/worldometer_death_rate_by_country.csv', index=False)
    
    # Grafik: Ölüm oranı en yüksek 10 ülke
    top10 = oran_tablosu.head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x='Olum_Orani', y='Country/Region', data=top10, palette='Reds')
    plt.title('Ülkelere Göre En Yüksek Ölüm Oranı (İlk 10)')
    plt.xlabel('Ölüm Oranı (%)')
    plt.ylabel('Ülke')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/worldometer_death_rate_top10.png')
    plt.close()
    print('Ülkelere göre ölüm oranı tablosu ve grafiği oluşturuldu.')

def gorsel_1_gunluk_yeni_vaka():
    df = oku_day_wise()
    plt.figure(figsize=(14,6))
    plt.plot(df['Date'], df['New cases'], color='orange')
    plt.title('Günlük Yeni Vaka Sayısı (Dünya Geneli)')
    plt.xlabel('Tarih')
    plt.ylabel('Yeni Vaka')
    # X eksenini seyrekleştir
    step = max(1, len(df)//14)
    plt.xticks(df['Date'][::step], rotation=45)
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/gorsel_1_gunluk_yeni_vaka.png')
    plt.close()

def gorsel_2_gunluk_yeni_olum():
    df = oku_day_wise()
    plt.figure(figsize=(14,6))
    plt.plot(df['Date'], df['New deaths'], color='red')
    plt.title('Günlük Yeni Ölüm Sayısı (Dünya Geneli)')
    plt.xlabel('Tarih')
    plt.ylabel('Yeni Ölüm')
    step = max(1, len(df)//14)
    plt.xticks(df['Date'][::step], rotation=45)
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/gorsel_2_gunluk_yeni_olum.png')
    plt.close()

def gorsel_3_kita_vaka_pasta():
    df = oku_worldometer()
    df = df.groupby('Continent')['TotalCases'].sum()
    plt.figure(figsize=(8,8))
    plt.pie(df, labels=df.index, autopct='%1.1f%%', startangle=140)
    plt.title('Kıtalara Göre Toplam Vaka Dağılımı')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/gorsel_3_kita_vaka_pasta.png')
    plt.close()

def gorsel_4_kita_olum_pasta():
    df = oku_worldometer()
    df = df.groupby('Continent')['TotalDeaths'].sum()
    plt.figure(figsize=(8,8))
    plt.pie(df, labels=df.index, autopct='%1.1f%%', startangle=140)
    plt.title('Kıtalara Göre Toplam Ölüm Dağılımı')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/gorsel_4_kita_olum_pasta.png')
    plt.close()

def gorsel_5_en_cok_test_yapan_ulkeler():
    df = oku_worldometer()
    df = df.fillna(0)
    top10 = df.sort_values('TotalTests', ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x='TotalTests', y='Country/Region', data=top10, palette='Blues')
    plt.title('En Çok Test Yapan 10 Ülke')
    plt.xlabel('Toplam Test')
    plt.ylabel('Ülke')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/gorsel_5_en_cok_test_yapan_ulkeler.png')
    plt.close()

def gorsel_6_en_yuksek_aktif_vaka():
    df = oku_worldometer()
    df = df.fillna(0)
    top10 = df.sort_values('ActiveCases', ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x='ActiveCases', y='Country/Region', data=top10, palette='Oranges')
    plt.title('En Yüksek Aktif Vaka Sayısına Sahip 10 Ülke')
    plt.xlabel('Aktif Vaka')
    plt.ylabel('Ülke')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/gorsel_6_en_yuksek_aktif_vaka.png')
    plt.close()

def gorsel_7_iyilesme_orani_top10():
    df = oku_worldometer()
    df = df.fillna(0)
    df = df[df['TotalCases'] > 0]
    df['Iyilesme_Orani'] = (df['TotalRecovered'] / df['TotalCases']) * 100
    top10 = df.sort_values('Iyilesme_Orani', ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x='Iyilesme_Orani', y='Country/Region', data=top10, palette='Greens')
    plt.title('İyileşme Oranı En Yüksek 10 Ülke')
    plt.xlabel('İyileşme Oranı (%)')
    plt.ylabel('Ülke')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/gorsel_7_iyilesme_orani_top10.png')
    plt.close()

def gorsel_8_haftalik_vaka_artis_orani():
    df = oku_country_latest()
    df = df.fillna(0)
    top10 = df.sort_values('1 week % increase', ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x='1 week % increase', y='Country/Region', data=top10, palette='Purples')
    plt.title('Haftalık Yeni Vaka Artış Oranı En Yüksek 10 Ülke')
    plt.xlabel('Haftalık Artış (%)')
    plt.ylabel('Ülke')
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/gorsel_8_haftalik_vaka_artis_orani.png')
    plt.close()

def gorsel_9_usa_county_top10():
    try:
        df = oku_usa_county()
        df = df.fillna(0)
        top10 = df.sort_values('Confirmed', ascending=False).head(10)
        plt.figure(figsize=(12,6))
        sns.barplot(x='Confirmed', y='Combined_Key', data=top10, palette='Reds')
        plt.title('ABD’de En Çok Vaka Görülen 10 County')
        plt.xlabel('Toplam Vaka')
        plt.ylabel('County')
        plt.tight_layout()
        plt.savefig('analiz_ciktisi/gorsel_9_usa_county_top10.png')
        plt.close()
    except Exception as e:
        print('usa_county_wise.csv için görsel oluşturulamadı:', e)

def gorsel_10_zaman_serisi_karsilastirma():
    df = oku_day_wise()
    plt.figure(figsize=(14,7))
    plt.plot(df['Date'], df['Confirmed'], label='Toplam Vaka', color='orange')
    plt.plot(df['Date'], df['Deaths'], label='Toplam Ölüm', color='red')
    plt.plot(df['Date'], df['Recovered'], label='Toplam İyileşen', color='green')
    plt.title('Zaman İçinde Toplam Vaka, Ölüm ve İyileşenler')
    plt.xlabel('Tarih')
    plt.ylabel('Kişi Sayısı')
    plt.legend()
    step = max(1, len(df)//14)
    plt.xticks(df['Date'][::step], rotation=45)
    plt.tight_layout()
    plt.savefig('analiz_ciktisi/gorsel_10_zaman_serisi_karsilastirma.png')
    plt.close()

if __name__ == "__main__":
    analiz_worldometer()
    death_rate_by_country()
    gorsel_1_gunluk_yeni_vaka()
    gorsel_2_gunluk_yeni_olum()
    gorsel_3_kita_vaka_pasta()
    gorsel_4_kita_olum_pasta()
    gorsel_5_en_cok_test_yapan_ulkeler()
    gorsel_6_en_yuksek_aktif_vaka()
    gorsel_7_iyilesme_orani_top10()
    gorsel_8_haftalik_vaka_artis_orani()
    gorsel_9_usa_county_top10()
    gorsel_10_zaman_serisi_karsilastirma() 