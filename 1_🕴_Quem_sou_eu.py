import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Quem sou eu ?",
    page_icon="🕴",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.markdown("Desenvolvido por Gustavo Gouvêa Soares *ggsgustavoggs@gmail.com*")

st.image("Geral\\eu.jpg", width=150)
st.write("# Gustavo Gouvêa Soares")
col1, col2 = st.columns(2)
col1.divider()

st.write("Sou um profissional focado em tecnologia e inovação, com interesse em desenvolvimento web, modelagem 3D e sistemas interativos. Tenho facilidade em aprender novas ferramentas e gosto de resolver desafios técnicos de forma criativa.")
st.write("Minha experiência inclui projetos que combinam programação e design, trazendo soluções funcionais e visualmente atraentes. Busco sempre aprimorar minhas habilidades e contribuir para equipes e projetos que valorizem a inovação.")
