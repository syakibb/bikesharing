import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("Dashboard Analisis Data Bike Sharing 🚲")
st.subheader("Data Harian & Per Jam - Capital Bikeshare Washington D.C.")

# Load data
df_day = pd.read_csv('dashboard/day_clean.csv')
df_hour = pd.read_csv('dashboard/hour_clean.csv')

# Sidebar untuk memilih dataset
dataset_option = st.sidebar.selectbox("Pilih Dataset", ("Data Harian", "Data Per Jam"))

# Load data sesuai pilihan
if dataset_option == "Data Harian":
    df = df_day.copy()
    st.write("### Dataset Harian")
else:
    df = df_hour.copy()
    st.write("### Dataset Per Jam")

# Filter Musim
season_option = st.selectbox('Pilih Musim:', df['season'].unique())

# Filter dataframe berdasarkan musim yang dipilih
filtered_df = df[df['season'] == season_option]

# Menampilkan metrik utama
total_peminjaman = filtered_df['cnt'].sum()
casual_total = filtered_df['casual'].sum()
registered_total = filtered_df['registered'].sum()

st.write("### Ringkasan Metrik")
col1, col2, col3 = st.columns(3)
col1.metric("Total Peminjaman", total_peminjaman)
col2.metric("Casual Users", casual_total)
col3.metric("Registered Users", registered_total)

# Visualisasi: Peminjaman per Bulan / Jam
st.write(f"### Jumlah Peminjaman Sepeda per Bulan/Jam di Musim {season_option}")

if dataset_option == "Data Harian":
    group_col = 'mnth'
    xlabel = 'Bulan'
else:
    group_col = 'hr'
    xlabel = 'Jam'

monthly_data = filtered_df.groupby(group_col)[['casual', 'registered']].sum()

fig, ax = plt.subplots(figsize=(10,6))
monthly_data.plot(kind='bar', stacked=True, ax=ax)
plt.title(f'Perbandingan Casual & Registered per {xlabel} - {season_option}')
plt.xlabel(xlabel)
plt.ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Visualisasi Korelasi Faktor Lingkungan
st.write("### Korelasi Faktor Lingkungan dengan Jumlah Peminjaman")

corr = filtered_df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()

fig2, ax2 = plt.subplots(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2)
plt.title('Correlation Matrix')
st.pyplot(fig2)

st.caption('Dashboard by Syakib 🚴‍♂️')
