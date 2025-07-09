import streamlit as st
import pandas as pd
import os
from PIL import Image
import zipfile
import io

st.set_page_config(page_title="COVID-19 Veri Analiz Web Uygulaması", layout="wide")
st.title("COVID-19 Veri Analiz Web Uygulaması")
st.markdown("""
Bu uygulama, COVID-19 verilerinin analizini ve görselleştirmesini sunar. Aşağıda özet tabloları ve grafiklerle verileri inceleyebilirsiniz.
""")

# Özet tabloları yükle
col1, col2 = st.columns(2)

with col1:
    st.header("En Çok Vaka Görülen 10 Ülke")
    try:
        df_cases = pd.read_csv("../analiz_ciktisi/worldometer_top_cases.csv")
        st.dataframe(df_cases)
    except:
        st.warning("Tablo yüklenemedi.")

with col2:
    st.header("En Çok Ölüm Görülen 10 Ülke")
    try:
        df_deaths = pd.read_csv("../analiz_ciktisi/worldometer_top_deaths.csv")
        st.dataframe(df_deaths)
    except:
        st.warning("Tablo yüklenemedi.")

st.header("Kıta Bazında Toplam Vaka ve Ölüm")
try:
    df_cont = pd.read_csv("../analiz_ciktisi/worldometer_continent_summary.csv")
    st.dataframe(df_cont)
except:
    st.warning("Tablo yüklenemedi.")

st.header("Analizlerden Seçili Grafikler")
gorsel_list = [
    "worldometer_top_cases.png",
    "worldometer_top_deaths.png",
    "worldometer_continent_cases.png",
    "worldometer_continent_deaths.png",
    "gorsel_1_gunluk_yeni_vaka.png",
    "gorsel_2_gunluk_yeni_olum.png",
    "gorsel_3_kita_vaka_pasta.png",
    "gorsel_4_kita_olum_pasta.png",
    "gorsel_5_en_cok_test_yapan_ulkeler.png",
    "gorsel_6_en_yuksek_aktif_vaka.png",
    "gorsel_7_iyilesme_orani_top10.png",
    "gorsel_8_haftalik_vaka_artis_orani.png",
    "gorsel_9_usa_county_top10.png",
    "gorsel_10_zaman_serisi_karsilastirma.png",
    "worldometer_death_rate_top10.png"
]

for gorsel in gorsel_list:
    gorsel_path = f"../analiz_ciktisi/{gorsel}"
    if os.path.exists(gorsel_path):
        st.image(Image.open(gorsel_path), use_column_width=True)
    else:
        st.warning(f"{gorsel} bulunamadı.")

# --- En alta veri setlerini indirme butonu ekle ---

st.markdown("---")
st.subheader(":file_folder: Kullanılan Tüm Veri Setlerini İndir")

# CSV dosyalarını zip'le
csv_files = [f for f in os.listdir("..") if f.endswith(".csv")]
zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, "w") as zipf:
    for csv in csv_files:
        with open(f"../{csv}", "rb") as f:
            zipf.writestr(csv, f.read())
zip_buffer.seek(0)

st.download_button(
    label="Tüm CSV Veri Setlerini ZIP Olarak İndir",
    data=zip_buffer,
    file_name="covid19_veri_setleri.zip",
    mime="application/zip",
    help="Kullanılan tüm veri setlerini tek tıkla indir."
) 