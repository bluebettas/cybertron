import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


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

st.markdown("<h1 style='text-align: center; '>The Bad Guy: Cyber Attack</h1>", unsafe_allow_html=True)
st.image("https://media.istockphoto.com/photos/computing-and-malware-concept-picture-id1127637966?k=20&m=1127637966&s=612x612&w=0&h=qoLN1myCQjRsfGZ1WyJTCtdnpojWeKT3KruSUlPpZx4=", width=700)
st.write("\n")
st.markdown("Seperti yang sudah dijelaskan di _page_ sebelumnya, _cyber attack_ itu kegiatan ilegal yang membahayakan. Nah, kira-kira seberapa bahaya sih _cyber attack_, siapa saja sih yang pernah jadi korban penjahat siber, dan kira-kira bagaimana kita bisa menjaga diri kita sendiri dari ancaman penjahat siber?")
st.info("Yuk baca halaman ini sampai akhir untuk menambah wawasan kamu!")

st.write("___________________________________________________")
st.header("Dampak Cyber Attack :gun:")
st.write("""Serangan siber dapat ditujukan pada level pemerintahan, sektor bisnis atau individual, dan tidak selalu terjadi dalam skala besar atau luas.
            Serangan siber dapat melumpuhkan sistem komputer yang berdampak pada :""")
with st.expander("1. Kerugian finansial pada perusahaan karena website mereka tidak bisa diakses."):
     st.image("https://media.istockphoto.com/photos/cyber-security-concept-internet-crime-hacker-working-on-a-code-and-picture-id1150199868?k=20&m=1150199868&s=612x612&w=0&h=yjoa5mZhTupb9e8mXKsNqsi6UBqekLkXzCJqpFvxq_A=")
 
with st.expander("2. Menghentikan badan pemerintahan dalam memberikan pelayanan esensial"):
     st.markdown("![Alt Text](https://i.ibb.co/WPS0kb3/Berita.png)")
 
with st.expander("3. Tercurinya data-data sensitif yang dapat merugikan individu pada tingkat finansial atau personal."):
     st.video("https://youtu.be/Ay8ByeoZUpA")
st.write("___________________________________________________") 

st.markdown("<h3 style='text-align: center; '>Bahaya Cyber Attack terhadap Perempuan dan Anak</h3>", unsafe_allow_html=True)
st.image("https://i.postimg.cc/jSK5P3TK/PASSWORD-CHECK-6.png", width=700)
st.write("Berdasarkan Badan Pusat Statistik dan Asosiasi Penyedia Jasa Internet (APJII), pengguna internet di Indonesia lebih banyak perempuan dibanding pria, masing-masing 51% dan 50,2%. Menurut hasil survei yang dilakukan oleh Kaspersky Lab dan B2B International, kaum perempuan pengguna internet kurang peduli untuk melindungi dirinya terhadap ancaman online dibanding laki-laki.")
st.image("https://i.postimg.cc/NF6t0Y5X/PASSWORD-CHECK-7.png", width=700)
st.write("Hanya 19% perempuan yang percaya bahwa mereka bisa menjadi korban penjahat cyber sementara satu dari empat pria (25%) menganggap hal tersebut mungkin terjadi. Selain itu, menurut survei para perempuan umumnya hanya sedikit mengetahui tentang ancaman cyber dibandingkan laki-laki. Sebagai contoh, 27% laki-laki dan 38% perempuan tidak menyadari ransomware; 23% laki-laki dan 34% perempuan sedikit mengetahui tentang malware ponsel; 21% laki-laki dan 34% perempuan memiliki pengetahuan yang terbatas mengenai apa itu eksploitasi. Kurangnya kesadaran ini menyebabkan perempuan kurang memberikan perhatian terhadap perlindungan diri dari ancaman cyber.")
st.image("https://i.postimg.cc/zGjQp7LT/PASSWORD-CHECK-10.png", width=700)
st.write("Sebanyak 30% penduduk Indonesia adalah anak-anak. Pesatnya perkembangan informasi dan teknologi mengakibatkan informasi dapat diakses dengan mudah dan cepat. Salah satu contoh kejahatan cyber yang bisa terjadi pada anak-anak yaitu scamming, perilaku yang dilakukan oleh seseorang untuk menipu orang lain sedang hits sekarang di kaum remaja adalah scammer cinta. Awalnya pelaku memajang foto seorang pria atau wanita yang menarik perhatian, lalu kenalan kemudian chatting dengan intensitas yang sering dan memberikan perhatian lebih. Kemudian dia minta bertemu lalu dirampok ataupun tidak bertemu tapi meminjam uang dengan berbagai alasan. Tentu setelah uang didapat, dia akan menghilang tanpa jejak. Oleh karena itu, perempuan dan anak-anak sangatlah rentan terhadap kejahatan cyber.")
st.write("___________________________________________________")

st.header("Cara Penanggulangannya :bulb:")
st.write("1. Memprioritaskan penggunaan *software* asli")
with st.expander("Apa kelebihan dari software asli?"):
     st.caption("""
        Meskipun harga *software* asli lebih mahal, kualitasnya tentu sebanding dengan biaya yang dikeluarkan. Selain itu juga bisa mendapatkan *update* otomatis secara resmi jika menggunakan *software* asli.
     """)
 
st.write("2. Melakukan update *Software* secara rutin")
with st.expander("Mengapa harus update Software rutin?"):
     st.caption("""
        Karena *software* terbaru biasanya sudah dilengkapi proteksi keamanan yang lebih baik dari versi *software* sebelumnya. Sehingga penggunaan *software* versi terbaru akan melindungi data diri dari incaran pelaku *cyber crime* serta risiko data hilang akibat virus pun semakin kecil kalau rajin melakukan *update software*.
     """)
 
st.write("3. Mengaktifkan *Data Encryption*")
with st.expander("Apa manfaat dari Data Encryption?"):
     st.caption("""
         Manfaat data *encryption* untuk melindungi data-data penting memang tak boleh dianggap remeh. Aktivasi data *encryption* akan mencegah akses yang berstatus tidak sah serta meminimalkan risiko penyadapan data.
     """)
 
st.write("4. Menerapkan konsep 2-*Factor Authentication (2-FA)*")
with st.expander("Apa itu 2-Factor Autentication?"):
     st.caption("""
         Konsep 2-*Factor Authentication* adalah suatu metode keamanan yang memungkinkan website melakukan verifikasi pengguna dengan kode yang langsung dikirim dalam waktu bersamaan (bersifat *real time*).
     """)
 
st.write("5. Menggunakan password yang unik")
with st.expander("Bagaimana membuat password yang unik?"):
     st.caption("""
         *Password* yang unik adalah salah satu cara mengatasi *cyber crime*. Kombinasi huruf besar, huruf kecil, angka, dan karakter pada password akan membuatnya lebih sulit diretas daripada password yang hanya terdiri dari huruf.
     """)
st.write("\n")
st.write("\n")

st.write("___________________________________________________")

st.subheader(":girl: : Ada ngga sih _website_ buat cek keamanan data kita?")
st.subheader(":female-scientist: : Ada nih... coba cek penjelasannya di bawah ini!")
st.video("https://youtu.be/eH6GbiJd944")
st.warning("Dapat dicoba pada website https://breachdirectory.org atau https://haveibeenpwned.com")
