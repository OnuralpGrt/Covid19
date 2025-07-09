from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Görsellerin ve CSV dosyalarının yolu
ANALIZ_CIKTISI_PATH = '../analiz_ciktisi'
CSV_PATH = '../'

def get_gorseller():
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
    mevcut_gorseller = [g for g in gorsel_list if os.path.exists(os.path.join(ANALIZ_CIKTISI_PATH, g))]
    return mevcut_gorseller

def get_csv_files():
    files = [f for f in os.listdir(CSV_PATH) if f.endswith('.csv')]
    return files

@app.route('/')
def index():
    gorseller = get_gorseller()
    csv_files = get_csv_files()
    return render_template('index.html', gorseller=gorseller, csv_files=csv_files)

@app.route('/gorsel/<filename>')
def gorsel(filename):
    return send_file(os.path.join(ANALIZ_CIKTISI_PATH, filename))

@app.route('/csv/<filename>')
def csv_file(filename):
    return send_file(os.path.join(CSV_PATH, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) 