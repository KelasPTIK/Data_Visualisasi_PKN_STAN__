import streamlit as st # type: ignore

st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/⚙️_General_Information_About_Data_Visualization.py", label="General Information About Data Visualization", icon="⚙️")
st.page_link("pages/⛏️_Tools_for_DataViz.py", label="Data Visualization Type", icon="⛏️")

st.header("**Data Dijelaskan Berdasarkan :red[Informasi] Yang Ingin Diberikan**")

st.subheader("A. Menunjukkan Perubahan :green[Waktu]")
genre = st.radio(
    "**1. Terdapat beberapa kumpulan data**",
    [":rainbow[Gunakan Line Chart]"],
    index=None
)
if genre == ":rainbow[Gunakan Line Chart]":
    st.image("https://www.jaspersoft.com/content/dam/jaspersoft/images/graphics/infographics/line-chart-example.svg", caption="Line Chart")

genre = st.radio(
    "**2. Data membentuk suatu kesatuan**",
    [":rainbow[Gunakan Stacked Area Chart]"],
    index=None
)
if genre == ":rainbow[Gunakan Stacked Area Chart]":
    st.image("https://datavizcatalogue.com/methods/images/top_images/stacked_area_graph.png", caption="Stacked Area Chart")

genre = st.radio(
    "**3. Semua kumpulan data mempunyai satuan ukuran yang sama**",
    [":rainbow[Gunakan Multiple Line Chart]"],
    index=None
)
if genre == ":rainbow[Gunakan Multiple Line Chart]":
    st.image("https://us.v-cdn.net/6031209/uploads/5W27T3OGIAXD/image.png", caption="Multiple Line Chart")

genre = st.radio(
    "**4. Semua kumpulan data tidak mempunyai satuan ukuran yang sama**",
    [":rainbow[Gunakan Combination Bar dan Line Chart]"],
    index=None
)
if genre == ":rainbow[Gunakan Combination Bar dan Line Chart]":
    st.image("https://community.qlik.com/legacyfs/online/143410_pastedImage_0.png", caption="Combination Bar dan Line Chart")


st.subheader("B. Membandingkan :blue[Perbedaan] dan :violet[Pengelompokan]")
genre = st.radio(
    "**1. hanya ada kategori non numerik**",
    [":rainbow[Gunakan Diagram Objek]"],
    index=None
)
if genre == ":rainbow[Gunakan Diagram Objek]":
    st.image("https://cdn-images.visual-paradigm.com/guide/uml/what-is-object-diagram/03-class-diagram-to-object-diagram.png", caption="Diagram Objek")

genre = st.radio(
    "**2. Semua angka ditampilkan**",
    [":rainbow[Gunakan Tabel]"],
    index=None
)
if genre == ":rainbow[Gunakan Tabel]":
    st.image("https://cdn-web.ruangguru.com/landing-pages/assets/hs/data%201.jpg", caption="Tabel")

genre = st.radio(
    "**3. Data merupakan bagian dari banyak data**",
    [":rainbow[Gunakan Stacked Bar]"],
    index=None
)
if genre == ":rainbow[Gunakan Stacked Bar]":
    st.image("https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/d135f39a-7d15-458c-a58d-cc35e304f9d4/9-stacked-bar-chart-final-large-opt.png", caption="Stacked Bar")

genre = st.radio(
    "**4. Data bukan merupakan bagian dari banyak data**",
    [":rainbow[Gunakan Small Multiples]"],
    index=None
)
if genre == ":rainbow[Gunakan Small Multiples]":
    st.image("https://upload.wikimedia.org/wikipedia/en/a/a6/Smallmult.png", caption="Small Multiples")

st.subheader("C. Menunjukkan Tren :red[Data Kuantitatif]")
genre = st.radio(
    "**1. Hubungan data perlu ditampilkan**",
    [":rainbow[Gunakan Scatter Plot]"],
    index=None
)
if genre == ":rainbow[Gunakan Scatter Plot]":
    st.image("https://files.planyway.com/strapi-uploads/assets/Scatter_plot_422d3c3f82.png", caption="Scatter Plot")

genre = st.radio(
    "**2. Hubungan data tidak perlu ditampilkan**",
    [":rainbow[Gunakan Box Plot]"],
    index=None
)
if genre == ":rainbow[Gunakan Box Plot]":
    st.image("https://www.simplypsychology.org/wp-content/uploads/compare-boxplots.jpg", caption="Box Plot")

st.subheader("D. Menyorot Sebuah :rainbow[Data]")
genre = st.radio(
    "**1. Informasi latar belakang diperlukan**",
    [":rainbow[Gunakan ScoreCard]"],
    index=None
)
if genre == ":rainbow[Gunakan ScoreCard]":
    st.image("https://www.panritaslide.com/wp-content/uploads/2023/02/BSC03.png", caption="ScoreCard")

genre = st.radio(
    "**2. Perubahan waktu ditamapilkan**",
    [":rainbow[Gunakan SparkLine]"],
    index=None
)
if genre == ":rainbow[Gunakan SparkLine]":
    st.image("https://www.ag-grid.com/_astro/sparklines-overview.CNaxBxC7.png", caption="SparkLine")

genre = st.radio(
    "**3. Perubahan waktu tidak perlu ditamapilkan**",
    [":rainbow[Gunakan BulletChart]"],
    index=None
)
if genre == ":rainbow[Gunakan BulletChart]":
    st.image("https://www.tableau.com/sites/default/files/2021-07/Bullet%20Graph%20-%20Good%20-%20900x650.png", caption="BulletChart")
		

# Menambahkan animasi teks bergerak dari kiri ke kanan
st.markdown("""
    <style>
        @keyframes moveRight {
            from {
                transform: translateX(-100%);
            }
            to {
                transform: translateX(100%);
            }
        }
        .animate-text {
            display: inline-block;
            font-size: 24px;
            animation: moveRight 5s linear infinite;
        }
    </style>
    <div style="text-align: center;">
        <span class="animate-text">Tipe Datanya Banyak Sekali🤔</span>
    </div>
    """, unsafe_allow_html=True)
