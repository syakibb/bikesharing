import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("Dashboard Analisis Penggunaan Sepeda 🚴‍♂️")
st.subheader("Capital Bikeshare Washington D.C. | Data Harian & Per Jam")

st.markdown("""
Dashboard ini menyajikan analisis data peminjaman sepeda dari Capital Bikeshare di Washington D.C.  
Gunakan filter musim dan dataset untuk mengeksplorasi tren pengguna casual & registered, serta pengaruh faktor lingkungan terhadap peminjaman sepeda.
""")

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

# Insight Box Dinamis
st.markdown("### 📌 Insight")
if casual_total > registered_total:
    st.info(f'Pada musim **{season_option}**, pengguna **casual** lebih banyak dibanding pengguna registered.')
else:
    st.success(f'Pada musim **{season_option}**, pengguna **registered** mendominasi peminjaman sepeda.')

# Diagram Pie: Casual vs Registered di filter musim
st.markdown("### 📊 Proporsi Pengguna Casual vs Registered")
pie_labels = ['Casual', 'Registered']
pie_sizes = [casual_total, registered_total]
pie_colors = ['#3498db', '#e67e22']

fig_pie, ax_pie = plt.subplots()
ax_pie.pie(pie_sizes, labels=pie_labels, colors=pie_colors, autopct='%1.1f%%', startangle=90)
ax_pie.axis('equal')
st.pyplot(fig_pie)

# Visualisasi: Peminjaman per Bulan / Jam
st.markdown(f"### 📈 Jumlah Peminjaman Sepeda per Bulan/Jam di Musim {season_option}")

if dataset_option == "Data Harian":
    group_col = 'mnth'
    xlabel = 'Bulan'
else:
    group_col = 'hr'
    xlabel = 'Jam'

monthly_data = filtered_df.groupby(group_col)[['casual', 'registered']].sum()

fig, ax = plt.subplots(figsize=(10,6))
monthly_data.plot(
    kind='bar', 
    stacked=True, 
    ax=ax, 
    color=['#3498db', '#e67e22']
)

plt.title(f'Perbandingan Casual & Registered per {xlabel} - {season_option}', fontsize=14, weight='bold')
plt.xlabel(xlabel, fontsize=12)
plt.ylabel('Jumlah Peminjaman', fontsize=12)
plt.legend(['Casual', 'Registered'], fontsize=10)
plt.xticks(rotation=0)
st.pyplot(fig)

# Visualisasi Korelasi Faktor Lingkungan
st.markdown("### 🔍 Korelasi Faktor Lingkungan dengan Jumlah Peminjaman")

corr = filtered_df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()

fig2, ax2 = plt.subplots(figsize=(8,6))
sns.heatmap(
    corr,
    annot=True,
    cmap='YlGnBu',
    linewidths=0.5,
    linecolor='white',
    square=True,
    cbar_kws={"shrink": .5},
    ax=ax2
)

plt.title('Matriks Korelasi Faktor Lingkungan dengan Jumlah Peminjaman', fontsize=14, weight='bold')
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
st.pyplot(fig2)

# Footer
st.caption('Dashboard by Syakib 🚴‍♂️')
