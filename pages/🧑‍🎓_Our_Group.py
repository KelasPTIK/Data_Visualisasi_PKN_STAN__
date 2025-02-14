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
        <span class="animate-text">⬇️Bisa Dicek Anggota-Anggota Yang Kece Di Bawah⬇️</span>
    </div>
    """, unsafe_allow_html=True)
# Menampilkan teks berwarna pink

# Menambahkan animasi getar pada tulisan menggunakan HTML + CSS
st.markdown("""
    <style>
        @keyframes shake {
            0% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            50% { transform: translateX(10px); }
            75% { transform: translateX(-10px); }
            100% { transform: translateX(0); }
        }
        .shake-header {
            animation: shake 0.5s ease-in-out infinite;
            color: pink;  /* Warna biru */
            font-size: 48px;
            text-align: center;  /* Menempatkan tulisan di tengah */
            font-weight: bold;
        }
    </style>
    
    <div class="shake-header">
        <h1>Our Beloved Member</h1>
    </div>
""", unsafe_allow_html=True)


from PIL import Image # type: ignore

# Path ke gambar lokal (ganti dengan path gambar yang sesuai)
image_path = "D:\Teknologi Informasi\Gambar kelompok PTIK.jpg"  # Contoh: "C:/Users/NamaUser/Pictures/gambar.jpg"

# Membuka gambar dengan PIL
img = Image.open(image_path)

# Menampilkan gambar
st.image(img, caption="Wajah-wajah Imut Nan Lucu", use_container_width=True)

st.markdown("<h1 style='text-align: center; color: red;'>MUHAMMAD FADHIL HAMDANI (4131240302)</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: blue;'>ADANNIS MAHTSANY TSAQIF (94131240265)</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: orange;'>DEVY GRACE NATALIE PADANG (4131240274)</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: green;'>SHOFIYYAH SALMA ISKANDAR (4131240356)</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: purple;'>NUR HALIZA (4131240327)</h1>", unsafe_allow_html=True)


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
        <span class="animate-text">🙏Kami Mohon Maaf atas keterbatasan dan Kemampuan Kami Dalam Membuat Web Ini🙏</span>
    </div>
    """, unsafe_allow_html=True)
