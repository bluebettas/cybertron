from turtle import left, title
import streamlit as st
import base64
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner 
import time
from streamlit_option_menu import option_menu

st.image("https://media.giphy.com/media/ILbo79w6XwR0axLYOw/giphy.gif", width=700)
st.markdown("<h3 style='text-align: center; '>Kenapa 'Cybertron'?</h3>", unsafe_allow_html=True)
st.markdown("""Cybertron merupakan salah satu
        planet dari serial "The Transformers"
        yang memiliki energi yang besar. 
        Harapan dari kelompok 3 dengan 
        menggunakan nama Cybertron, kami bisa 
        memberikan energi besar dan mengedukasi 
        masyarakat mengenai _cyber security_.""")
st.image("https://media.giphy.com/media/C0jD15xeqdcTGrMex2/giphy.gif", width=700)

selected = option_menu(
    menu_title =  None,
    options = ("Naila", "Yusri", "Zahra"),
    orientation = ("horizontal"),
    icons=["1-square", "2-square", "3-square"],
    )
if selected == "Naila":
    st.image("https://media.giphy.com/media/cGUu1UjzDlDoUD6riz/giphy.gif", width=700)
    st.markdown("<h1 style='text-align: center; '>Naila Cahayani Putri</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; '>19 Tahun</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>Mahasiswi Semester 5 Fakultas Psikologi Universitas Airlangga</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>Surabaya, Jawa Timur</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; '>Empowered Women empower Women.</h6>", unsafe_allow_html=True)
    st.write("___________________________________________________________")
    st.markdown("<h6 style='text-align: left; '>Contact Info:</h6>", unsafe_allow_html=True)
    c1, c2 = st.columns([1,12])
    with c1:
        st.image("https://www.designbust.com/download/171/png/instagram_logo_color_icon256.png", width = 30)
    with c2:
        st.write("@nailaacp")

if selected == "Yusri":
    st.image("https://media.giphy.com/media/2vV4jtesg5Fn70WJYf/giphy.gif", width = 700)
    st.markdown("<h1 style='text-align: center; '>Yusriana Chusna Fadilah</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; '>20 Tahun</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>Mahasiswi Semester 5 Sistem Informasi Universitas Nasional</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>Ciracas, Jakarta</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; '>Maka sesungguhnya bersama kesulitan itu ada kemudahan✨</h6>", unsafe_allow_html=True)
    st.write("___________________________________________________________")
    st.markdown("<h6 style='text-align: left; '>Contact Info:</h6>", unsafe_allow_html=True)
    y1, y2 = st.columns([1,12])
    with y1:
        st.image("https://www.designbust.com/download/171/png/instagram_logo_color_icon256.png", width = 30)
    with y2:
        st.write("@yusrianachus_")
   
if selected == "Zahra":
    st.image("https://media.giphy.com/media/URBadwOhXBC6aGHtPv/giphy.gif", width = 700)
    st.markdown("<h1 style='text-align: center; '>Zahra Alhumairah Basa</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; '>20 Tahun</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>Mahasiswi Semester 5 Pendidikan Matematika Universitas Sriwijaya</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>Palembang, Sumatera Selatan</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; '>Be a cupcake in a world of muffins 🧁</h6>", unsafe_allow_html=True)
    st.write("___________________________________________________________")
    st.markdown("<h6 style='text-align: left; '>Contact Info:</h6>", unsafe_allow_html=True)
    z1, z2 = st.columns([1,12])
    with z1:
        st.image("https://www.designbust.com/download/171/png/instagram_logo_color_icon256.png", width = 30)
    with z2:
        st.write("@zhralhb")