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

st.markdown("<h1 style='text-align: center; '>Introduction to Cybersecurity</h1>", unsafe_allow_html=True)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
 
lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_zdtukd5q.json"
lottie_url_download = "https://assets9.lottiefiles.com/packages/lf20_zdtukd5q.json"
lottie_hello = load_lottieurl(lottie_url_hello)
 
_left, mid, _right = st.columns(3)
with mid:
    st_lottie(lottie_hello, key="hello")


st.write("________________________________________________________________________________")
st.subheader("Apa itu Cyber Security:question::question::question:")
 
st.caption("Sebelum itu, coba jawab pertanyaan di bawah ini :smile:")
pengalaman = st.radio(
     "Apakah kalian pernah mendengar Cyber Security?",
     ('Pernah', 'Belum Pernah', 'Ragu'))
 
if pengalaman == 'Pernah':
     st.write('Keren! :star::star::star: Mari kita menambah wawasan lagi mengenai Cyber Security :smile:')
else:
     st.write("Mari kita kenali lebih dalam mengenai Cyber Security ya! :fire:")
 
 
st.info("Ayo kita bahas sobat Cybertron! :smile:")
 
_left, mid, _right = st.columns(3)
with _left:
    st.image("https://binus.ac.id/wp-content/uploads/2020/10/43-0-Kupas-Tuntas-Jurusan-Cyber-Security.-Belajar-Apa-Saja-sih-di-Kampus.jpg", width = 700)
 
st.write("Cyber security adalah tindakan dalam melindungi program, data, jaringan, maupun sistem teknologi yang dilakukan oleh individu atau institusi dari risiko cyberattacks.")
st.write("Langkah yang perlu dilakukan dalam cyber security yaitu memberikan proteksi yang lebih kuat dari cyberattacks seperti memiliki banyak lapisan perlindungan pada perangkat komputer, jaringan, maupun data program yang dijaga oleh keamanan yang kuat")
st.write("Ancaman cyber security bisa datang dari internal maupun eksternal institusi. Ancaman yang berasal dari internal bisa datang dari karyawan maupun anggota institusi, sedangkan ancaman yang berasal dari eksternal bisa datang dari pelaku kejahatan cyberattack")
st.write("________________________________________________________________________________")

st.subheader("Sejarah Cyber Security")
st.write("Sejarah awal dari Cyber Security yaitu dimulai pada tahun 1970-an yang pada saat itu peneliti yang bernama Bob Thomas menciptakan program komputer yang diberi nama Creeper. Creeper berfungsi untuk memindahkan program antar sistem yang dihubungkan oleh ARPANET (Advanced Research Projects Agency Network)")
st.write("Selain itu, Ray Tomlinson seorang penemu email menciptakan program yang diberi nama Reaper dan memiliki pengkodean versi program yang lebih tinggi sehingga bisa menghapus Creeper. Reaper merupakan contoh software antivirus pertama yang dapat mereplikasi diri dalam sistem komputer")
 
st.warning("Silakan menonton video agar lebih paham :tv:")
st.video("https://youtu.be/Ml4bgx8ZN9Q")
 
_left, mid, _right = st.columns(3)
with mid:
     st.text("Sumber: Channel Youtube JSON SEC")

st.markdown("*Terjemahan: :gear: > Subtitel/CC > Terjemahkan Otomatis > Indonesia")
st.write("________________________________________________________________________________")
 
st.subheader("Konsep Dasar Cyber Security")
st.write("Konsep dasar cyber security mengikuti praktik dari CIA Triad (model standar dalam keamanan informasi) yang meliputi:")
st.write("1. Confidentiality")
 
with st.expander("Apa itu Confidentiality?"):
     st.write("""
         Confidentiality merupakan tindakan dalam menjaga atau merahasiakan sebuah informasi maupun data agar tidak terjadi kebocoran dan pencurian data.
         Contohnya bisa menggunakan Two Factor Authentication (2FA) yang memiliki dua tahap yaitu tahap pertama menggunakan password dan tahap kedua menggunakan kode khusus yang akan dikirimkan ke perangkat tertentu.
     """)
     st.image("https://www.imperva.com/learn/wp-content/uploads/sites/13/2019/01/2fa-example.jpg")
 
st.write("2. Integrity")
 
with st.expander("Apa itu Integrity?"):
     st.write("""
         Integrity merupakan tindakan untuk memastikan semua data akurat, konsisten, dan terpercaya ketika akan diakses oleh pengguna.
         Contohnya bisa menggunakan enkripsi, tanda tangan digital, maupun Certificate Authority (CA) digital sebagai verifikasi identitas pengguna.
     """)
     st.image("https://www.domainesia.com/asset/uploads/2021/05/Screen-Shot-2021-05-24-at-12.09.43-PM-1024x412.png")
 
st.write("3. Availability")
 
with st.expander("Apa itu Availability?"):
     st.write("""
         Availability merupakan tindakan untuk memastikan ketersediaan data dan pengguna bisa mengakses data dengan mudah.
     """)
     st.image("https://qph.cf2.quoracdn.net/main-qimg-9718fd63d7fcf468aa96e5241ab72056-lq")
st.write("________________________________________________________________________________")

st.subheader("Beberapa Jenis Cyber Security")
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    st.write("Network Security (Keamanan Jaringan)")
    st.image("https://kworld.com.gh/wp-content/uploads/2019/08/Data-and-network-security.png")
 
with col2:
    st.write("Application Security (Keamanan Aplikasi)")
    st.image("https://miro.medium.com/max/1000/1*MHUHYCYkjggUrmkbZg9_7Q.jpeg")
 
with col3:
    st.write("Cloud Security (Keamanan Cloud)")
    st.image("https://i.ytimg.com/vi/JyQ_NHwA0QI/maxresdefault.jpg")
 
with col4:
    st.write("Operational Security (Keamanan Operasional)")
    st.image("https://www.erdalozkaya.com/wp-content/uploads/2021/06/OpSec.png")
st.write("________________________________________________________________________________")

st.title("Cyber Attack")
_left, mid, _right = st.columns(3)
with mid:
   st.image("https://c.tenor.com/LhbkIA2jc94AAAAd/together-we-can-protect-our-election-system-from-cyber-attack-vrl.gif")
st.write("Cyberattack merupakan kegiatan ilegal yang dilakukan menggunakan peralatan, jaringan komputer, maupun kode komputer yang memiliki sifat yang merusak, mencuri, mengubah, mengganggu, menutup akses, mengurangi kinerja dari komputer atau jaringan komputer secara sengaja dan melawan hukum.")
 
st.title("Beberapa Bentuk Cyber Attack")
 
st.write("1. Phishing")
 
with st.expander("Apa itu Phishing?"):
     st.write("""
         Phishing yaitu ketika attackers berusaha mencuri data sensitif korban dengan cara menyamar sebagai institusi legal dan menghubungi mereka melalui email, telepon, maupun pesan teks.
     """)
     st.image("https://psti.unisayogya.ac.id/wp-content/uploads/2020/09/7351a3eaf347208cbe75e46466551474.jpg")
 
st.write("2. Malware")
 
with st.expander("Apa itu Malware?"):
     st.write("""
         Malware merupakan program maupun file yang dibuat bertujuan untuk mengeksploitasi atau merusak perangkat, server, maupun jaringan.
     """)
     st.image("https://www.niagahoster.co.id/blog/wp-content/uploads/2018/09/apa-itu-malware-site-ahead-contains-malware-1024x488.png")
 
st.write("3. Social Engineering")
 
with st.expander("Apa itu Social Engineering?"):
     st.write("""
         Social Engineering yaitu pelaku mengeksploitasi aspek psikologi korban dan mendorongnya untuk memberikan informasi personal maupun akses terhadap perangkatnya.
     """)
     st.image("http://student-activity.binus.ac.id/himsisfo/wp-content/uploads/sites/16/2017/03/social-engineering.jpg")
st.write("________________________________________________________________________________") 
 
st.title("Indeks Keamanan Siber Negara-Negara Asia Tenggara (2022)")
st.text("Sumber: National Cyber Security Index, 7 Maret 2022")
 
 
import pandas as pd
import numpy as np
import altair as alt
 
 
source = pd.DataFrame({
     'Skala 0-100': [79.22, 71.43, 64.94, 63.64, 41.56, 38.96, 36.36, 18.18, 15.58, 10.39],
     'Negara-Negara Asia Tenggara': ['Malaysia','Singapura', 'Thailand', 'Filipina', 'Brunei Darussalam', 'Indonesia', 'Vietnam', 'Laos', 'Kamboja', 'Myanmar']
})
 
bar_chart = alt.Chart(source).mark_bar().encode(
     y='Skala 0-100',
     x= 'Negara-Negara Asia Tenggara',
)
st.altair_chart(bar_chart, use_container_width=True)
 
st.write("___________________________________")
st.text("Referensi:")
st.text("Equifax. 2022. How Cyber Attacks Happen. https://www.equifax.co.uk/resources/identity-protection/how-cyber-attacks-happen.html")
st.text("Nagitec. 2020. Cyver Attack dan Upaya Mencegahnya. https://nagitec.com/cyber-attack-dan-upaya-mencegahnya/")

