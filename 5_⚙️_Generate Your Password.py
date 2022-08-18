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

##Password Generator
st.header("Kamu juga bisa coba _password generator_ yang kita sediakan!")
st.image("https://i.ibb.co/qgDWjvm/PASSWORD-CHECK-5.png", width=700)
import random
import array
## Range panjang password, di sini pakai 8-16 karakter
MAX_LEN = st.slider("Masukkan panjang password yang diinginkan (8 - 16):", 8, 16)

## Memasukkan karakter
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

## Menyatukan
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

## Memilih at least 1 karakter random dari gabungan karakter di atas
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

## Dikombinasikan
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

p3 = ""
for x in temp_pass_list:
		p3 = p3 + x
		
## Hasil password generator
import time
with st.spinner(text='Tunggu sebentar ya...'):
    time.sleep(0.5)
    st.info(p3)

st.write("________________________________________________")
st.image("https://media.giphy.com/media/ZhvYpCYiMtpgPbt7c5/giphy.gif", width=700)