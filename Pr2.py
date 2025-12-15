import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# ==============================
# TRANSLATIONS
# ==============================
translations = {
    "en": {
        "page_title": "Survey Analyzer",
        "language": "Language / Bahasa",
        "select_language": "Select Language",
        "navigation": "Navigation",
        "select_page": "Select Page",
        "home": "Home",
        "survey_analyzer": "Survey Analyzer",
        "sidebar_info": "📊 **Survey Analyzer**\n\nAnalyze survey data using descriptive statistics and correlation analysis.\n\nIndustrial Engineering Student Project",
        "home_title": "Survey Analyzer",
        "home_subtitle": "Analyze survey data using descriptive statistics and correlation analysis",
        "features": "Features",
        "features_list": "- Descriptive statistics\n- Pearson correlation analysis\n- Modern neon dashboard UI\n- Likert-scale survey support\n- CSV upload from Google Form",
        "survey_title": "Survey Analysis",
        "case_study": "Case Study:",
        "case_study_desc": "Group Chat Usage and Group Task Effectiveness",
        "analysis_method": "Analysis Method: Descriptive Statistics & Pearson Correlation",
        "upload_dataset": "Upload Dataset",
        "upload_desc": "Upload CSV file from Google Form",
        "error_missing_columns": "❌ **Error:** The uploaded CSV is missing required columns.",
        "missing_x": "Missing X items:",
        "missing_y": "Missing Y items:",
        "overview": "Overview",
        "total_respondents": "Total Respondents",
        "total_x": "Total X",
        "total_y": "Total Y",
        "mean_x": "Mean X (Group Chat Usage)",
        "mean_y": "Mean Y (Task Effectiveness)",
        "pearson_summary": "Pearson Correlation Summary",
        "correlation_coeff": "Correlation Coefficient (r)",
        "p_value": "p-value",
        "dataset_preview": "Dataset Preview",
        "descriptive_stats": "Descriptive Statistics",
        "pearson_analysis": "Pearson Correlation Analysis",
        "person_correlation": "Full Pearson Correlation Matrix",
        "relationship_text": "✅ There is a **{strength}, {direction}**, and **{sig}** relationship between **Group Chat Usage (X)** and **Group Task Effectiveness (Y)**.",
        "statistically_significant": "statistically significant",
        "not_statistically_significant": "not statistically significant",
        "weak": "weak",
        "moderate": "moderate",
        "strong": "strong",
        "positive": "positive",
        "negative": "negative",
        "footer": "Survey Analyzer • Industrial Engineering Student Project"
    },
    "id": {
        "page_title": "Analisis Survei",
        "language": "Bahasa / Language",
        "select_language": "Pilih Bahasa",
        "navigation": "Navigasi",
        "select_page": "Pilih Halaman",
        "home": "Beranda",
        "survey_analyzer": "Analisis Survei",
        "sidebar_info": "📊 **Analisis Survei**\n\nAnalisis data survei menggunakan statistik deskriptif dan analisis korelasi.\n\nProyek Mahasiswa Teknik Industri",
        "home_title": "Analisis Survei",
        "home_subtitle": "Analisis data survei menggunakan statistik deskriptif dan analisis korelasi",
        "features": "Fitur",
        "features_list": "- Statistik deskriptif\n- Analisis korelasi Pearson\n- UI dashboard neon modern\n- Dukungan skala Likert\n- Unggah CSV dari Google Form",
        "survey_title": "Analisis Survei",
        "case_study": "Studi Kasus:",
        "case_study_desc": "Penggunaan Group Chat dan Efektivitas Tugas Kelompok",
        "analysis_method": "Metode Analisis: Statistik Deskriptif & Korelasi Pearson",
        "upload_dataset": "Unggah Dataset",
        "upload_desc": "Unggah file CSV dari Google Form",
        "error_missing_columns": "❌ **Error:** CSV yang diunggah kehilangan kolom yang diperlukan.",
        "missing_x": "Item X yang hilang:",
        "missing_y": "Item Y yang hilang:",
        "overview": "Ringkasan",
        "total_respondents": "Total Responden",
        "total_x": "Total X",
        "total_y": "Total Y",
        "mean_x": "Rata-rata X (Penggunaan Group Chat)",
        "mean_y": "Rata-rata Y (Efektivitas Tugas)",
        "pearson_summary": "Ringkasan Korelasi Pearson",
        "correlation_coeff": "Koefisien Korelasi (r)",
        "p_value": "p-value",
        "dataset_preview": "Pratinjau Dataset",
        "descriptive_stats": "Statistik Deskriptif",
        "pearson_analysis": "Analisis Korelasi Pearson",
        "person_correlation": "Matriks Korelasi Pearson Lengkap",
        "relationship_text": "✅ Ada hubungan **{strength}, {direction}**, dan **{sig}** antara **Penggunaan Group Chat (X)** dan **Efektivitas Tugas Kelompok (Y)**.",
        "statistically_significant": "secara statistik signifikan",
        "not_statistically_significant": "tidak secara statistik signifikan",
        "weak": "lemah",
        "moderate": "sedang",
        "strong": "kuat",
        "positive": "positif",
        "negative": "negatif",
        "footer": "Analisis Survei • Proyek Mahasiswa Teknik Industri"
    }
}

def get_text(key, lang="en"):
    return translations[lang].get(key, key)

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Survey Analyzer",
    page_icon="📊",
    layout="wide"
)

# ==============================
# CUSTOM CSS (DARK NEON UI)
# ==============================
st.markdown("""
<style>
    body {
        background-color: #0b1220;
        color: white;
    }

    .block-container {
        padding: 2rem;
    }

    .title-box {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 35px;
        border-radius: 22px;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 140, 255, 0.5);
        margin-bottom: 30px;
    }

    .section {
        background-color: #0f172a;
        padding: 25px;
        border-radius: 20px;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
    }

    .metric-box {
        background-color: #111827;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 0 15px rgba(0, 200, 255, 0.3);
        text-align: center;
    }

    .highlight {
        color: #38bdf8;
        font-weight: bold;
    }

    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR
# ==============================
lang = "en"  # Default language
st.sidebar.markdown(f"## 🌐 {get_text('language', lang)}")
lang = st.sidebar.selectbox(get_text("select_language", lang), ["en", "id"], format_func=lambda x: "English" if x == "en" else "Bahasa Indonesia")

st.sidebar.markdown("---")
st.sidebar.markdown(f"## 📌 {get_text('navigation', lang)}")
menu = st.sidebar.radio(
    get_text("select_page", lang),
    [get_text("home", lang), get_text("survey_analyzer", lang)]
)

st.sidebar.markdown("---")
st.sidebar.info(get_text("sidebar_info", lang))

# ==============================
# HOME PAGE
# ==============================
if menu == get_text("home", lang):
    st.markdown(f"""
    <div class="title-box">
        <h1>📊 {get_text('home_title', lang)}</h1>
        <p>{get_text('home_subtitle', lang)}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    ### ✨ {get_text('features', lang)}
    {get_text('features_list', lang)}
    """)

# ==============================
# SURVEY ANALYZER PAGE
# ==============================
if menu == get_text("survey_analyzer", lang):

    # HERO TITLE
    st.markdown(f"""
    <div class="title-box">
        <h1>📊 {get_text('survey_title', lang)}</h1>
        <p><b>{get_text('case_study', lang)}</b> {get_text('case_study_desc', lang)}</p>
        <p>{get_text('analysis_method', lang)}</p>
    </div>
    """, unsafe_allow_html=True)

    # FILE UPLOAD
    st.markdown(f"### 📂 {get_text('upload_dataset', lang)}")
    uploaded_file = st.file_uploader(
        get_text("upload_desc", lang),
        type=["csv"]
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # ==============================
        # VARIABLE ITEMS
        # ==============================
        X_items = [
            'Saya aktif menggunakan group chat (WhatsApp/Telegram/LINE/Discord) untuk berbagai aktivitas sehari-hari.',
            'Saya mengikuti lebih dari satu group chat, baik untuk kuliah, hobi, maupun komunitas.',
            'Group chat membantu saya mendapatkan informasi penting (tugas, event, jadwal, pengumuman).',
            'Saya sering menggunakan group chat untuk berdiskusi, baik tentang akademik maupun non-akademik.',
            'Saya merasa group chat memudahkan komunikasi dalam berbagai kegiatan seperti belajar, gaming, atau organisasi.',
            'Saya sering bergantung pada group chat untuk mengetahui update terbaru.'
        ]

        Y_items = [
            'Saya mudah berkomunikasi dengan anggota kelompok melalui platform group chat.',
            'Group chat membuat koordinasi tugas kelompok menjadi lebih efisien.',
            'Saya dapat berbagi file, link, dan informasi dengan mudah melalui group chat selama kerja kelompok.',
            'Diskusi dalam group chat membantu memperjelas pembagian tugas dalam kelompok.',
            'Kolaborasi kelompok saya menjadi lebih teratur karena adanya komunikasi lewat group chat.',
            'Tugas kelompok lebih cepat diselesaikan karena adanya komunikasi yang lancar melalui group chat.'
        ]

        # ==============================
        # VALIDATE COLUMNS
        # ==============================
        missing_X = [item for item in X_items if item not in df.columns]
        missing_Y = [item for item in Y_items if item not in df.columns]

        if missing_X or missing_Y:
            st.error(get_text("error_missing_columns", lang))
            if missing_X:
                st.write(f"{get_text('missing_x', lang)} {missing_X}")
            if missing_Y:
                st.write(f"{get_text('missing_y', lang)} {missing_Y}")
            st.stop()

        # ==============================
        # COMPOSITE SCORES
        # ==============================
        df["X_total"] = df[X_items].sum(axis=1)
        df["Y_total"] = df[Y_items].sum(axis=1)

        # ==============================
        # OVERVIEW METRICS
        # ==============================
        st.markdown(f"## 📌 {get_text('overview', lang)}")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(get_text("total_respondents", lang), df.shape[0])
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(get_text("total_x", lang), int(df["X_total"].sum()))
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(get_text("total_y", lang), int(df["Y_total"].sum()))
            st.markdown('</div>', unsafe_allow_html=True)

        with col4:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(get_text("mean_x", lang), round(df["X_total"].mean(), 2))
            st.markdown('</div>', unsafe_allow_html=True)

        with col5:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(get_text("mean_y", lang), round(df["Y_total"].mean(), 2))
            st.markdown('</div>', unsafe_allow_html=True)

        # ==============================
        # PEARSON CORRELATION SUMMARY
        # ==============================
        r, p = pearsonr(df["X_total"], df["Y_total"])

        st.markdown(f"### 🔗 {get_text('pearson_summary', lang)}")
        corr_table = pd.DataFrame({
            "Metric": [get_text("correlation_coeff", lang), get_text("p_value", lang)],
            "Value": [f"{r:.3f}", f"{p:.6f}"]
        })
        st.table(corr_table)

        # ==============================
        # DATASET PREVIEW
        # ==============================
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader(f"📄 {get_text('dataset_preview', lang)}")
        st.dataframe(df, width='stretch')
        st.markdown('</div>', unsafe_allow_html=True)

        # ==============================
        # DESCRIPTIVE STATISTICS
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader(f"📊 {get_text('descriptive_stats', lang)}")

        desc = df[X_items + Y_items + ["X_total", "Y_total"]].describe().T
        desc = desc[["mean", "std", "min", "50%", "max"]]
        desc.rename(columns={"50%": "median"}, inplace=True)

        st.dataframe(desc, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ==============================
        # PERSON CORRELATION MATRIX
        # ==============================
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader(f"🔗 {get_text('person_correlation', lang)}")

        corr_matrix = df.select_dtypes(include=[np.number]).corr()
        st.dataframe(corr_matrix, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ==============================
        # PEARSON CORRELATION
        # ==============================
        r, p = pearsonr(df["X_total"], df["Y_total"])

        if p < 0.05:
            sig = get_text("statistically_significant", lang)
        else:
            sig = get_text("not_statistically_significant", lang)

        if abs(r) < 0.3:
            strength = get_text("weak", lang)
        elif abs(r) < 0.6:
            strength = get_text("moderate", lang)
        else:
            strength = get_text("strong", lang)

        direction = get_text("positive", lang) if r > 0 else get_text("negative", lang)

        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader(f"🔗 {get_text('pearson_analysis', lang)}")

        st.markdown(f"""
        - **{get_text('correlation_coeff', lang)}:** <span class="highlight">{r:.3f}</span>
        - **{get_text('p_value', lang)}:** <span class="highlight">{p:.6f}</span>
        """, unsafe_allow_html=True)

        st.markdown(
            get_text("relationship_text", lang).format(strength=strength, direction=direction, sig=sig)
        )

        st.markdown('</div>', unsafe_allow_html=True)

    # ==============================
    # FOOTER
    # ==============================
    st.markdown(f"""
    <hr>
    <center>
    <p style="color:gray;">{get_text('footer', lang)}</p>
    </center>
    """, unsafe_allow_html=True)
