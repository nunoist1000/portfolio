import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")


st.title("👔Resume")

with open('resume.md', 'r') as markdown_file:
    resume_markdown = markdown_file.read()

st.markdown(resume_markdown, unsafe_allow_html=True)

st.write("[Click here if it's blocked by your browser](https://drive.google.com/file/d/1fVJ1Y9GhKAFDmf4hY6STTACHHVzT9MY8/view?usp=sharing)")

with open('images/Dev.pdf', 'rb') as pdf_file:
    pdf_bytes = pdf_file.read()
    st.download_button(label="Download Resume as PDF",
                       data=pdf_bytes,
                       file_name="My_Resume.pdf",
                       mime='application/octet-stream')

  


