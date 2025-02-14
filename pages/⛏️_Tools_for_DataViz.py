import streamlit as st # type: ignore

st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/⚙️_General_Information_About_Data_Visualization.py", label="General Information About Data Visualization", icon="⚙️")


st.header("Tools for :green[DataViz]")
st.subheader("**1. Power :red[BI]**")
st.markdown(
    """
    <style>
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .animated-text {
        font-size: 24px;
        font-weight: normal;
        animation: slideIn 1.5s ease-out;
    }
    </style>
    
    <p class="animated-text">Power BI adalah tool dari Microsoft yang juga cukup populer di kalangan data scientist dan business analyst. Tool ini terintegrasi dengan baik dengan produk Microsoft lainnya seperti Excel dan SQL Server. Salah satu keunggulan Power BI adalah kemampuannya dalam menyediakan visualisasi interaktif serta laporan real-time yang bisa diakses di berbagai perangkat, termasuk ponsel. Selain itu, Power BI juga menawarkan kemampuan untuk membuat dashboard yang sangat intuitif dan mudah dipahami.</p>
    """,
    unsafe_allow_html=True
)


st.subheader("**2. Tableau**")
st.markdown(
    """
    <style>
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .animated-text {
        font-size: 24px;
        font-weight: normal;
        animation: slideIn 1.5s ease-out;
    }
    </style>
    
    <p class="animated-text">Tableau adalah salah satu tools visualisasi data yang paling populer dan sering digunakan. Kelebihannya adalah kemampuan untuk memproses dan menganalisis data dalam jumlah besar tanpa penurunan performa. Visualisasi yang dilakukan adalah mengubah data tabel yang kaku menjadi bentuk grafik, diagram, geo mapping, dan sebagainya yang mampu memperlihatkan perubahan dan perbedaan data menjadi lebih jelas.</p>
    """,
    unsafe_allow_html=True
)
st.subheader("**3. Plotly**")
st.markdown(
    """
    <style>
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .animated-text {
        font-size: 24px;
        font-weight: normal;
        animation: slideIn 1.5s ease-out;
    }
    </style>
    
    <p class="animated-text">Plotly adalah tool yang bisa digunakan dalam berbagai bahasa pemrograman seperti Python, R, dan JavaScript. Keunggulan Plotly adalah kemampuannya untuk membuat visualisasi interaktif yang bisa di-zoom, di-slice, atau diatur sesuai keinginan pengguna. Ini sangat cocok digunakan ketika ingin membuat presentasi atau dashboard yang memungkinkan pengguna berinteraksi langsung dengan data.</p>
    """,
    unsafe_allow_html=True
)
st.subheader("**4. Visme**")
st.markdown(
    """
    <style>
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .animated-text {
        font-size: 24px;
        font-weight: normal;
        animation: slideIn 1.5s ease-out;
    }
    </style>
    
    <p class="animated-text">Visme adalah tools visualisasi data yang menawarkan berbagai template dan elemen desain yang dapat digunakan untuk membuat infografis, presentasi, dan laporan visual. Visme cocok untuk pengguna yang ingin membuat visualisasi data yang menarik tanpa harus memiliki keahlian desain grafis yang mendalam.</p>
    """,
    unsafe_allow_html=True
)
st.subheader("**5. Fushion :blue[Chart]**")
st.markdown(
    """
    <style>
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .animated-text {
        font-size: 24px;
        font-weight: normal;
        animation: slideIn 1.5s ease-out;
    }
    </style>
    
    <p class="animated-text">FusionCharts adalah pustaka grafik JavaScript yang memungkinkan pengembang untuk menghasilkan visualisasi data dari sumber data mereka, dengan lebih dari 100 jenis grafik dan 2.000 peta yang berbeda untuk dipilih. FusionCharts sangat berguna bagi orang-orang yang bekerja dengan data kompleks, karena intuitif dan mudah digunakan.</p>
    """,
    unsafe_allow_html=True
)
st.subheader("**6. Keylines**")
st.markdown(
    """
    <style>
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .animated-text {
        font-size: 24px;
        font-weight: normal;
        animation: slideIn 1.5s ease-out;
    }
    </style>
    
    <p class="animated-text">KeyLines adalah perangkat JavaScript yang digunakan oleh pengembang untuk membangun aplikasi visualisasi jaringan yang kuat, dengan cepat dan merupakan aplikasi dalam kategori pengembangan. Ada lebih dari 25 alternatif untuk KeyLines Graph Visualization Toolkit untuk berbagai platform, termasuk aplikasi berbasis Web, Windows, Self-Hosted, Linux, dan Mac.</p>
    """,
    unsafe_allow_html=True
)

st.page_link("pages/📊_Data_Visualization_Type.py", label="Data Visualization Type", icon="📊")

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
        <span class="animate-text">❤️Belajar DataViz Itu Menyenangkan dan Mudah❤️</span>
    </div>
    """, unsafe_allow_html=True)