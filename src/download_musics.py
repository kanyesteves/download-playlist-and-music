import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Baixar música"
)



st.title("Baixar música do Youtube")
tab1, tab2= st.tabs(["Playlist", "Vídeo"])

with tab1:
    st.text_input("Link para download da playlist")
    st.download_button(label="Download playlist", data="TESTE", file_name='requirements.txt')

with tab2:
    st.text_input("Link para download do vídeo")
    col1, col2 = st.columns([0.11,1])
    btn_convert = col1.button("Converter para MP3")
    col2.download_button(label="Download", data="TESTE", file_name='requirements.txt')

