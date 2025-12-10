import streamlit as st

# halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih aplikasi', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran'])

if menu == 'Luas Persegi':
    st.write(':blue[ini halaman untuk menghitung Luas Persegi]:balloon::balloon:')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi.jpg.webp', caption='gambar persegi')
    def luaspersegi(a):
        return a*a 
    sisi = st.number_input('masukan sisi persegi', min_value=0)

    if st.button('hitung'):
        luas = luaspersegi(sisi)
        st.write(f'luas persegi adalah {luas}')

elif menu == "Luas Segitiga":
    st.write(':blue[ini halaman untuk menghitung Luas Segitiga]:balloon::balloon:')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/06/rumus-luas-segitiga-sama-sisi.jpg', caption=gambar segitiga)
