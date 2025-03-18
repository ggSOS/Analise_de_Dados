import streamlit as st

st.set_page_config(
    page_title="Skills",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.markdown("Desenvolvido por Gustavo Gouvêa Soares *ggsgustavoggs@gmail.com*")

st.write("# Skills")
col1, col2 = st.columns(2)
col1.divider()

st.write(" ")
st.write(" ")
st.write(" ")
st.write("## Idiomas")
st.divider()
col1, col2 = st.columns(2)
col1.write(" ")
col1.write("**Inglês**")
col1.write("Compreende Razoavelmente, Fala Razoavelmente, Lê Razoavelmente, Escreve Pouco.")

col2.write(" ")
col2.write("**Espanhol**")
col2.write("Compreende Razoavelmente, Fala Pouco, Lê Razoavelmente, Escreve Pouco.")

st.write(" ")
st.write(" ")
st.write(" ")
st.write("## Linguagens Relacionadas à Tecnologia")
st.divider()
col1, col2 = st.columns(2)
col1.write(" ")
col1.write(" ")
col1.write("**Python**")
col1.write("Tanto para criação de APIs como para gerenciamento de banco de dados, desenvolvimento do front-end ou programas interativos por menus")
col1.write("Destaques: Flask, SQLite3, Streamlit e Menu Interativo")

col2.write(" ")
col2.write(" ")
col2.write("**Java**")
col2.write("Tanto para gerenciamento de banco de dados como lançamento de APIs")
col2.write("Destaques: JDBC e Spring Boot")

col1, col2 = st.columns(2)
col1.write(" ")
col1.write(" ")
col1.write("**JavaScript**")
col1.write("Destaques: JS puro e React")

col2.write(" ")
col2.write(" ")
col2.write("**PHP**")
col2.write("Destaque: PHP puro")

col1, col2 = st.columns(2)
col1.write(" ")
col1.write(" ")
col1.write("**HTML + CSS**")
col1.write("Para marcação e estilização de sites")
col1.write("Destaques: Tailwind e BOOTSTRAP")

col2.write(" ")
col2.write(" ")
col2.write("**SQL**")
col2.write("Para gerenciamento de banco de dados")
col2.write("Destaque: Oracle e SQLite3")

col1, col2 = st.columns(2)
col1.write(" ")
col1.write(" ")
col1.write("**C#**")
col1.write("Destaque: C# puro")

col2.write(" ")
col2.write(" ")
col2.write("**C++**")
col2.write("Para conectar e programar dispositivos periféricos como sensores")
col2.write("Destaque: Arduino e ESP32")

st.write(" ")
st.write(" ")
st.write("**C**")
st.write("Destaque: C puro")

st.write(" ")
st.write(" ")
st.write(" ")
st.write("## Modelagem, Texturização e Animação")
st.divider()
st.write("- Habilidade razoável com Maya 2025")
st.write("- Habilidade razoável com Substance Painter")
st.write("- Habilidade inicial com Unreal Engine")