import streamlit as st # type: ignore

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
        <span class="animate-text">🏆Selamat Datang di Web Terbaik Buatan ASPATH 1-7🏆</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; color: blue; margin-bottom: -20px;'>AYO BELAJAR VISUALISASI DATA</h1>
    <h1 style='text-align: center; color: yellow; margin-top: -30px;'>BERSAMA KAMI</h1>
    """, unsafe_allow_html=True)



st.markdown(
    """
    <style>
    .glow-img {
        display: block;
        margin: auto;
        width: 700px; /* Ukuran sangat besar */
        border-radius: 10px;
        box-shadow: 0px 0px 25px rgba(0, 0, 255, 0.8); /* Glow biru lebih kuat */
        transition: box-shadow 0.3s ease-in-out;
    }
    .glow-img:hover {
        box-shadow: 0px 0px 50px rgba(0, 0, 255, 1); /* Glow super terang saat hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<img src="https://dibimbing-cdn.sgp1.cdn.digitaloceanspaces.com/1685633396018-Jenis%20Visualisasi%20Data%20Dan%20Fungsinya%20yang%20Wajib%20Kamu%20Tahu.jpg.webp" class="glow-img">', unsafe_allow_html=True)


st.write("---------------------------------------------------------------------------------------------------------------------")
st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/⚙️_General_Information_About_Data_Visualization.py", label="General Information About Data Visualization", icon="⚙️")
st.page_link("pages/⛏️_Tools_for_DataViz.py", label="Tools for DataViz", icon="⛏️")
st.page_link("pages/📊_Data_Visualization_Type.py", label="Data Visualization Type", icon="📊")
st.page_link("pages/🧑‍🎓_Our_Group.py", label="Our Group", icon="🧑‍🎓")



