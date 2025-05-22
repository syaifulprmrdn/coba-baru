import streamlit as st

st.sidebar.title("Navigasi")
halaman = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Tentang", "Gambar"])

if halaman == "Beranda":
    st.title("Halo, Dunia!")
    st.write("Ini adalah halaman beranda.")

elif halaman == "Tentang":
    st.title("Tentang Aplikasi")
    st.write("Aplikasi ini dibuat dengan Streamlit dan mendukung banyak halaman!")

elif halaman == "Gambar":
    st.title("Halaman Gambar")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/June_odd-eyed-cat.jpg/320px-June_odd-eyed-cat.jpg",
        caption="Kucing lucu!",
        use_column_width=True
