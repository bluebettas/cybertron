from turtle import left
import streamlit as st
import base64
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner 
import time
from streamlit_option_menu import option_menu

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
st.image("https://i.postimg.cc/N0Dd7jzD/PASSWORD-CHECK-8.png", width=700)
st.markdown("<h1 style='text-align: center; '>Mari Uji Pengetahuanmu!</h1>", unsafe_allow_html=True)
 
st.caption("Ayo dijawab pertanyaan di bawah ini :smile:")
langkah = st.radio(
     "1. Langkah apa yang perlu dilakukan dalam Cyber Security?",
     ('Tidak perlu melakukan apa-apa', 'Memberikan proteksi yang lebih kuat dari cyberattacks'))
 
if langkah == 'Memberikan proteksi yang lebih kuat dari cyberattacks':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
creeper = st.radio(
     "2. Siapakah yang menciptakan program komputer yang diberi nama Creeper?",
     ('Ray Tomlinson', 'Bob Thomas'))
 
if creeper == 'Bob Thomas':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
confident = st.radio(
     "3. Tindakan dalam menjaga atau merahasiakan sebuah informasi maupun data agar tidak terjadi kebocoran dan pencurian data merupakan konsep dari?",
     ('Integrity', 'Confidentiality','Availability'))
 
if confident == 'Confidentiality':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
cyberattack = st.radio(
     "4. Apa itu Cyberattack?",
     ('Kegiatan legal yang dilakukan menggunakan peralatan, jaringan komputer, maupun kode komputer yang memiliki sifat yang merusak, mencuri, mengubah, mengganggu, menutup akses, mengurangi kinerja dari komputer atau jaringan komputer secara sengaja dan melawan hukum', 'Kegiatan ilegal yang dilakukan menggunakan peralatan, jaringan komputer, maupun kode komputer yang memiliki sifat yang merusak, mencuri, mengubah, mengganggu, menutup akses, mengurangi kinerja dari komputer atau jaringan komputer secara sengaja dan melawan hukum'))
 
if cyberattack == 'Kegiatan ilegal yang dilakukan menggunakan peralatan, jaringan komputer, maupun kode komputer yang memiliki sifat yang merusak, mencuri, mengubah, mengganggu, menutup akses, mengurangi kinerja dari komputer atau jaringan komputer secara sengaja dan melawan hukum':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
malware = st.radio(
     "5. Program maupun file yang dibuat bertujuan untuk mengeksploitasi atau merusak perangkat, server, maupun jaringan disebut sebagai?",
     ('Social Engineering', 'Malware', 'Phishing'))
 
if malware == 'Malware':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
langkah = st.radio(
     "6. Salah satu dampak Cyber Attack pada pelayanan pemerintahan?",
     ('Kesehatan', 'Kemiskinan' ))
 
if langkah == 'Kesehatan':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
creeper = st.radio(
     "7. Mengapa masih banyak orang yang tidak menggunakan software asli?",
     ('Karena mahal harga belinya', 'Karena jelek kualitasnya'))
 
if creeper == 'Karena mahal harga belinya':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
confident = st.radio(
     "8. Metode keamanan yang memungkinkan website melakukan verifikasi pengguna dengan kode yang langsung dikirim disebut?",
     ('Data Encryption', '2-Factor Autentication'))
 
if confident == '2-Factor Autentication':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
cyberattack = st.radio(
     "9. Manfaat adanya Data Encryption yaitu?",
     ('Mencegah akses yang tidak sah','Menghilangkan virus'))
 
if cyberattack == 'Mencegah akses yang tidak sah':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
malware = st.radio(
     "10. Contoh penerapan password yang kuat berikut adalah?",
     ('womenintech2', 'Womenintech#2', 'Womenintech#'))
 
if malware == 'Womenintech#2':
     st.success('Benar!:star:')
else:
     st.error("Salah :cry:")
     st.stop()
 
with st.spinner('Loading'):
    time.sleep(5)
st.image("https://media.giphy.com/media/wrFGDuJ4uoZ7nXr85U/giphy.gif", width=700)
 
st.balloons()
