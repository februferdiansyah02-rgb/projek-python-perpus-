import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman
st.set_page_config(page_title="Netflix Data Dashboard", layout="wide")

# --- LOAD DATA ---
@st.cache_data # Menggunakan cache agar loading lebih cepat
def load_data():
    df = pd.read_csv("netflix.csv")
    # Membersihkan data sederhana
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
    df['release_year'] = df['release_year'].astype(int)
    return df

df = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=200)
    st.title("Filter Panel")
    
    
    
    # Filter Tipe
    types = st.multiselect("Pilih Tipe Konten:", options=df['type'].unique(), default=df['type'].unique())
    
    # Filter Tahun
    year_range = st.slider("Rentang Tahun Rilis:", 
                           int(df['release_year'].min()), 
                           int(df['release_year'].max()), 
                           (2010, 2021))

# Filter Data Berdasarkan Input Sidebar
df_filtered = df[(df['type'].isin(types)) & (df['release_year'].between(year_range[0], year_range[1]))]

# --- JUDUL UTAMA ---
st.title("NETFLIX SI FER")
st.markdown(f"Menampilkan data dari tahun **{year_range[0]}** hingga **{year_range[1]}**")
st.divider()

# --- METRICS (KPIs) ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Judul", len(df_filtered))
col2.metric("Negara Terbanyak", df_filtered['country'].mode()[0] if not df_filtered.empty else "N/A")
col3.metric("Rata-rata Tahun Rilis", int(df_filtered['release_year'].mean()))

# --- KONTEN UTAMA ---
tab1, tab2 = st.tabs(["📊 Visualisasi", "📑 Raw Data"])

with tab1:
    # Baris 1: Distribusi Negara & Tipe
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Top 10 Negara Asal")
        top_countries = df_filtered['country'].value_counts().head(10)
        fig, ax = plt.subplots()
        sns.barplot(x=top_countries.values, y=top_countries.index, palette="Reds_r", ax=ax)
        ax.set_xlabel("Jumlah Konten")
        st.pyplot(fig)

    with c2:
        st.subheader("Distribusi Tipe Konten")
        type_counts = df_filtered['type'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=['#E50914', '#221F1F'], startangle=90)
        st.pyplot(fig)

    # Baris 2: Tren Tahun
    st.subheader("📈 Tren Rilis Konten Per Tahun")
    trend_data = df_filtered.groupby('release_year').size()
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(trend_data.index, trend_data.values, marker='o', color='#E50914', linewidth=2)
    ax.fill_between(trend_data.index, trend_data.values, color="#09E5D6", alpha=0.1)
    ax.set_title("Jumlah Rilis per Tahun")
    st.pyplot(fig)
    
    
with tab2:
    st.subheader("Preview Data Terfilter")
    st.dataframe(df_filtered, use_container_width=True)
    
    # Download Button
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button("Download Data as CSV", data=csv, file_name="netflix_filtered.csv", mime="text/csv")
    
    

# --- FOOTER ---
st.caption("Dibuat dengan  menggunakan Streamlit & Pandas")