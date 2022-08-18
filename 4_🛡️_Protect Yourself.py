from string import digits
from time import time
import streamlit as st
import re
import time

with st.sidebar:
    add_image = st.image("https://media.giphy.com/media/QiRT3QqDNPMlXVDxUo/giphy.gif")
    add_subheader = st.subheader("Cybertron")
    add_Write = st.write("""
        Cybertron merupakan salah satu
        planet dari serial "The Transformers"
        yang memiliki energi yang besar. 
        Harapan dari kelompok 3 dengan 
        menggunakan nama cybertron, kami bisa 
        memberikan energi besar dan mengedukasi 
        masyarakat mengenai cyber security.
    """)
    add_subheader = st.subheader("Find us on:")
    add_image = st.image("https://www.designbust.com/download/171/png/instagram_logo_color_icon256.png", width = 50)
    add_write = st.text("""
    Naila: @nailaacp
    Yusri: @yusrianachus_
    Zahra: @zhralhb""")

# Quiz sederhana
st.markdown("<h1 style='text-align: center; '>Tahukah Kamu?</h1>", unsafe_allow_html=True)
st.image("https://i.ibb.co/m01NHP1/PASSWORD-CHECK-1.png")
quiz = st.radio(
    "9 dari 10 Masyarakat Indonesia...",
    ('Memiliki pengetahuan yang baik mengenai cybersecurity',
    'Memiliki gadget terbaru',
    'Menggunakan kombinasi password yang tergolong lemah'))
if quiz =='Menggunakan kombinasi password yang tergolong lemah':
    st.success('Benar sekali! Menurut survey yang dilakukan oleh YouGov dan Google Indonesia, 89% masyarakat Indonesia masih mempertahankan penggunaan password yang lemah')
    st.image("https://i.postimg.cc/x1Y3dbfC/PASSWORD-CHECK-2.png", width=700)
else:    
    st.error('Belum tepat nih, coba pilih opsi lain!')
    st.stop()
st.write("___________________________________________________")

#Password checker v1
st.subheader("Yuk, kita cek seberapa kuat kombinasi _password_ kamu")
st.image("https://i.postimg.cc/PrW0cTpG/PASSWORD-CHECK.png", width=700)
p1 = st.text_input('Masukkan password disini:')
if not p1:
    st.warning('Silahkan masukkan password kamu.')
    st.stop()
elif (len(p1) < 8 or
    re.search('[0-9]',p1) is None or
    re.search('[A-Z]',p1) is None or
    re.search('[^a-zA-Z0-9]',p1) is None):
    st.error("Yah.. password kamu masih lemah!")
    time.sleep(0.5)
    st.info("Scroll down untuk mengetahui cara memperbaikinya, ya!")
st.write("___________________________________________________")

# Konten edukasi bahaya dari weak password
st.image("https://i.postimg.cc/wBLN5f4k/PASSWORD-CHECK-3.png", width=700)
st.subheader("Cek penjelasannya di bawah ini!")
with st.expander("Bahaya password yang lemah"):
     st.image("https://media.giphy.com/media/PIK1wPFzBgVmiDs0qr/giphy.gif", width=670)
     st.video("https://youtu.be/M3trBDRev4s")
     st.markdown("Menurut Danny Pehar, seorang spesialis kesadaran _cybersecurity_, pembatas antara diri kita dan penjahat di dunia maya adalah kata sandi yang kita buat sendiri, lho! Jadi, kamu udah kebayang belum seberapa krusialnya _password_ kamu untuk melindungi keamanan data pribadi kamu dari bahaya serangan penjahat siber?")

# Konten edukasi cara meningkatkan kekuatan password
with st.expander("Tips untuk membuat dan memperkuat password"):
     st.image("https://media.giphy.com/media/wkhmd8U4WWb2aEDpvY/giphy.gif", width=670)
     st.video("https://www.youtube.com/watch?v=IhlXtBNNuKs")
     st.markdown("*Terjemahan: :gear: > Subtitel/CC > Terjemahkan Otomatis > Indonesia")
     st.write("___________________________________________________")
     st.image("https://media.giphy.com/media/t7rUHD0wOFRPQ0bhr9/giphy.gif", width=670)
     col1, col2 = st.columns(2)
     col1.subheader(":white_check_mark: Do's :white_check_mark:")
     with col1:
        st.markdown(":one: Pastikan _password_ kamu terdiri dari minimal 8 karakter")
        st.markdown(":two: Pastikan _password_ kamu memiliki angka di dalamnya")
        st.markdown(":three: Pastikan _password_ kamu terdiri dari campuran huruf kapital dan huruf kecil")
        st.markdown(":four: Pastikan _password_ kamu juga punya karakter spesial (,./!@#$%&*_+-=) di dalamnya")
        st.markdown(":five: Ganti _password_ kamu secara berkala atau ketika kamu mengetahui adanya upaya peretasan")
     col2.subheader(":x: Dont's :x:")
     with col2:
        st.markdown(":one: Menggunakan identitas diri sendiri (contoh: nama dan tanggal lahir) dalam membuat _password_")
        st.markdown(":two: Membagikan informasi mengenai akun dan _password_ milikmu")
        st.markdown(":three: Menggunakan 1 _password_ untuk banyak akun")
        st.markdown(":four: Menggunakan password yang sama selamanya.")
# Semacam post test untuk mengaplikasikan pengetahuan yang didapat user
# dari konten edukasi di atas
with st.expander("Yuk coba praktikkan pengetahuan yang telah kamu dapatkan di sini!"):
     st.image("https://i.postimg.cc/SKhFRRBx/PASSWORD-CHECK-4.png", width=700)     
     p2 = st.text_input('Masukkan password kamu di sini:')
     if not p2:
        st.warning('Silahkan masukkan password kamu.')
        st.stop()
     if len(p2) < 8:
        st.error("Pastikan password terdiri dari 8 karakter")
        st.stop()
     elif re.search('[0-9]',p2) is None:
        st.error("Pastikan password memiliki angka di dalamnya")
        st.stop()
     elif re.search('[A-Z]',p2) is None: 
        st.error("Pastikan password memiliki huruf kapital di dalamnya")
        st.stop()
     elif re.search('[a-z]',p2) is None: 
        st.error("Pastikan password memiliki huruf kecil di dalamnya")
        st.stop()
     elif re.search('[^a-zA-Z0-9]',p2) is None:
        st.error("Pastikan password memiliki karakter spesial seperti !@#$%^&*()_+=-?/.,><';")
        st.stop()
     else:
        st.success("Password kamu sudah aman!" )
        st.balloons()
        time.sleep(0.5)
st.write("___________________________________________________")
