
# 🚲 Proyek Analisis Data Bike Sharing

Repository ini berisi proyek analisis data yang dikerjakan oleh **Syakib Binnur** untuk submission kelas **Belajar Analisis Data dengan Python** di Dicoding.

Dashboard analisis telah dibuat menggunakan **Streamlit** dan dapat diakses secara interaktif melalui link berikut:  
👉 [Dashboard Streamlit Cloud](https://bikesharing-syakib.streamlit.app/)

---

## 📄 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis **Bike Sharing Dataset** dari Capital Bikeshare Washington D.C.  
Analisis ini mengeksplorasi faktor-faktor yang mempengaruhi peminjaman sepeda, pola penggunaan oleh pengguna casual dan registered, serta tren musiman.

Output utama dari proyek ini meliputi:  
✅ **Exploratory Data Analysis (EDA)**  
✅ **Visualization & Explanatory Analysis**  
✅ **Analisis Lanjutan (Clustering Manual - Binning)**  
✅ **Dashboard Interaktif dengan Streamlit**

---

## 🗂️ Struktur Direktori

```
submission/
├── data/
│   ├── day.csv
│   └── hour.csv
├── dashboard/
│   ├── dashboard.py
│   ├── day_clean.csv
│   └── hour_clean.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## ⚙️ Instalasi

1. **Clone repository** ke komputer lokal:
```
git clone https://github.com/syakibb/bikesharing.git
```

2. **Pindah ke direktori project:**
```
cd bikesharing
```

3. **Install library yang dibutuhkan:**
```
pip install -r requirements.txt
```

---

## 🚀 Penggunaan

### 1. Jalankan Notebook Analisis  
Buka **notebook.ipynb** untuk melihat keseluruhan proses analisis data:  
✅ Data Wrangling  
✅ EDA  
✅ Visualization & Explanatory Analysis  
✅ Clustering Manual  
✅ Insight dan Kesimpulan

Jalankan di **Jupyter Notebook** atau **Google Colab** (dengan upload folder terlebih dahulu).

---

### 2. Jalankan Dashboard Streamlit di Lokal
```
cd submission
streamlit run dashboard/dashboard.py
```

Atau kunjungi **Dashboard Online di Streamlit Cloud**:  
👉 [https://bikesharing-syakib.streamlit.app/](https://bikesharing-syakib.streamlit.app/)

---

## 📊 Insight Utama dari Analisis
- **Suhu dan musim** adalah faktor utama yang mempengaruhi peminjaman sepeda.  
- Pengguna **registered** mendominasi sepanjang tahun, sementara **casual users** meningkat signifikan di musim Summer.  
- Clustering manual mengelompokkan hari ke dalam **Low**, **Medium**, dan **High Usage**, dengan mayoritas hari termasuk **Medium Usage**.

---

## 🧑‍💻 Author
- **Nama**: Syakib Binnur  
- **Email**: syakibb19@gmail.com  
- **Dicoding ID**: syakib  
- **GitHub**: [https://github.com/syakibb](https://github.com/syakibb)

---

## 📎 Link Penting
- Repository GitHub: [https://github.com/syakibb/bikesharing](https://github.com/syakibb/bikesharing)  
- Streamlit Cloud: [https://bikesharing-syakib.streamlit.app/](https://bikesharing-syakib.streamlit.app/)

---

🚴‍♂️ Terima kasih!
