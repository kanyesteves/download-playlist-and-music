import streamlit as st
import subprocess

st.set_page_config(
    layout="wide",
    page_title="YouTube Download"
)

# Check: https://docs.streamlit.io/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app

st.title("Download from YouTube")
tab1, tab2 = st.tabs(["Vídeo", "Playlist"])

with tab1:
    url = st.text_input(label="Link para download do vídeo", placeholder="https://www.youtube.com/watch?v=3KtWfp0UopM")
    col1, col2 = st.columns([0.11,1])
    col1.download_button(label="Download Video", data=f"{st}", file_name='requirements.txt')
    btn_convert = col2.button("Download MP3", disabled=True)

with tab2:
    st.text_input("Link para download da playlist", placeholder="https://www.youtube.com/playlist?list=PL590L5WQmH8fmto8QIHxA9oU7PLVa3ntk")
    st.download_button(label="Download playlist", data="TESTE", file_name='requirements.txt', disabled=True)