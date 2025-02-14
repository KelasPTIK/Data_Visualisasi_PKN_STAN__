import streamlit as st # type: ignore

st.page_link("Home.py", label="Home", icon="🏠")


st.header("Apa Itu Visualisasi :green[Data?]")
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
    
    <p class="animated-text">Visualisasi data adalah proses menggunakan elemen visual seperti diagram, grafik, atau peta untuk merepresentasikan data. Visualisasi data menerjemahkan yang kompleks, bervolume tinggi, atau numerik menjadi representasi visual yang lebih mudah diproses. Alat visualisasi data meningkatkan dan mengotomatiskan proses komunikasi visual untuk mendapatkan akurasi dan detail.</p>
    """,
    unsafe_allow_html=True
)

st.header("Mengapa Visualisasi Data Begitu :red[Penting?]")
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
    
    <p class="animated-text">Visualisasi membantu kita meningkatkan pemahaman terhadap data yang kompleks. Ketika data disajikan dalam bentuk visual, otak kita bisa lebih cepat menangkap pola, tren, dan anomali, dibandingkan jika kita harus menganalisis data mentah yang biasanya berupa angka atau teks. Hal ini tentunya sangat berguna dalam mempercepat proses pengambilan keputusan. Selain itu, visualisasi data memudahkan komunikasi informasi. Dalam situasi di mana waktu adalah hal yang sangat berharga, seperti dalam dunia bisnis atau riset, menyajikan data dalam bentuk visual membantu menyederhanakan informasi yang kompleks, sehingga mudah dipahami oleh berbagai kalangan, bahkan mereka yang tidak memiliki latar belakang teknis.</p>
    """,
    unsafe_allow_html=True
)

st.header("Apa Saja Manfaat Visualisasi :blue[Data?]")

st.subheader("**1. Pembuatan keputusan yang strategis**")

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
    
    <p class="animated-text">Pemangku kepentingan utama dan manajemen tingkat atas menggunakan visualisasi data untuk menafsirkan data dengan jelas. Mereka akan menghemat waktu dengan analisis data yang lebih cepat dan kemampuan untuk memvisualisasikan gambaran yang lebih besar. Misalnya, mereka dapat mengidentifikasi pola, menemukan tren, dan mendapatkan wawasan agar tetap terdepan dalam kompetisi.</p>
    """,
    unsafe_allow_html=True
)
st.subheader("**2. Peningkatan layanan pelanggan**")

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
    
    <p class="animated-text">Visualisasi data menyoroti kebutuhan dan keinginan pelanggan melalui representasi grafis. Anda dapat mengidentifikasi kesenjangan dalam layanan pelanggan Anda, meningkatkan produk atau layanan secara strategis, dan mengurangi inefisiensi operasional.</p>
    """,
    unsafe_allow_html=True
)
st.subheader("**3. Peningkatan keterlibatan karyawan**")

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
    
    <p class="animated-text">Teknik visualisasi data berguna untuk mengomunikasikan hasil analisis data kepada tim besar. Seluruh grup dapat memvisualisasikan data bersama untuk mengembangkan tujuan dan rencana yang sama. Mereka dapat menggunakan analitik visual untuk mengukur tujuan dan progres serta meningkatkan motivasi tim. Misalnya, tim penjualan bekerja sama untuk meningkatkan tinggi diagram batang penjualan mereka dalam satu kuartal</p>
    """,
    unsafe_allow_html=True
)
st.page_link("pages/⛏️_Tools_for_DataViz.py", label="Tools for DataViz", icon="⛏️")

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
        <span class="animate-text">🪼Ubur-Ubur Ikan Lele, Capek Buatnya Lee🦈</span>
    </div>
    """, unsafe_allow_html=True)