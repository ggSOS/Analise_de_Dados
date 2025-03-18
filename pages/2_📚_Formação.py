import streamlit as st

st.set_page_config(
    page_title="Formação",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.markdown("Desenvolvido por Gustavo Gouvêa Soares *ggsgustavoggs@gmail.com*")

st.write("# Formação Acadêmica")
col1, col2 = st.columns(2)
col1.divider()

col1, col2 = st.columns(2)
col1.write(" ")
col1.write("Graduação em Engenharia de Software")
col1.write("2023 - 2027")
col1.write("**FIAP**")

col2.write(" ")
col2.write("Graduação Tecnológica em Análise e Desenvolvimento de Sistemas")
col2.write("2023 - 2025")
col2.write("**SENAC**")

st.write(" ")
st.write("Ensino Médio Completo")
st.write("2018 - 2020")
st.write("**Colégio Davina Gasparini**")