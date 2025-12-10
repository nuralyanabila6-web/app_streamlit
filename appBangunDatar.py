import streamlit as st

# halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih aplikasi', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran', 'Luas Jajar Genjang'])

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
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/06/rumus-luas-segitiga-sama-sisi.jpg', caption='gambar segitiga')
    def Luassegitiga(a, t):
        return 0.5*a*t
    alas = st.number_input('masukan alas segitiga', min_value=0)
    tinggi = st.number_input('masukan tinggi segitiga', min_value=0)
    sisi_miring = st.number_input('masukan sisi miring segitiga', min_value=0)
    
    if st.button('hitung'):
        luas = Luassegitiga(alas, tinggi)
        st.write(f'Luas segitiga adalah {luas}')

elif menu == "Luas Lingkaran":
    st.write(':blue[ini halaman untuk menghitung luas lingkaran]:balloon::balloon:')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/06/rumus-luas-lingkaran.jpg', caption='gambar lingkaran')
    def luaslingkaran(r):
        return 3.14*r*r
    jari_jari = st.number_input('masukan jari-jari lingkaran', min_value=0)

    if st.button('hitung'):
        luas = luaslingkaran(jari_jari)
        st.write(f'luas lingkaran adalah {luas}')

elif menu == "Luas Persegi Panjang":
    st.write(':blue[ini halaman untuk menghitung Luas Persegi Panjang]:balloon::balloon:')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi-panjang.jpg.webp', caption='gambar persegi panjang')
    def luaspersegipanjang(p, l):
        return p*l
    panjang = st.number_input('masukan panjang persegi panjang', min_value=0)
    lebar = st.number_input('masukan lebar persegi panjang', min_value=0)

    if st.button('hitung'):
        luas = luaspersegipanjang(panjang, lebar)
        st.write(f'luas persegi panjang adalah {luas}')

