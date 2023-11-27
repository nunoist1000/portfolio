import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from constant import *
from PIL import Image
import openai
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title='Landing Zone' ,layout="wide",page_icon='📝')

# -----------------  chatbot  ----------------- #
# Set up the OpenAI key
openai_api_key = st.secrets['OPENAI_API_KEY']
openai.api_key = (openai_api_key)

notion = Image.open("images/notion.jpg")
ghub = Image.open("images/github.png")
linked = Image.open("images/linkedin.png")
# load the file
documents = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()

pronoun = info["Pronoun"]
name = info["Name"]
def ask_bot(input_text):
    # define LLM
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=openai.api_key,
    )
    llm_predictor = LLMPredictor(llm=llm)
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    
    # load index
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)    
    
    # query LlamaIndex and GPT-3.5 for the AI's response
    PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {name} in his job search by providing recruiters with relevant and concise information. 
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}. 
    Don't put "Buddy" or a breakline in the front of your answer.
    Human: {input}
    """
    
    output = index.as_query_engine().query(PROMPT_QUESTION.format(input=input_text))
    print(f"output: {output}")
    return output.response

# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You can send your questions and hit Enter to know more about me from my AI agent, Buddy!", key="input")
    return input_text

#st.markdown("Chat With Me Now")
user_input = get_text()

if user_input:
  #text = st.text_area('Enter your questions')
  if not openai_api_key.startswith('sk-'):
    st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
  if openai_api_key.startswith('sk-'):
    st.info(ask_bot(user_input))

    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# loading assets
lottie_gif = load_lottieurl("https://lottie.host/9b0af794-88be-4af1-b728-80508b884f55/r7isyhm6Ub.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")



# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#003366', '#000000', '#FFA500',f"Hi, I'm {full_name}📖", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    st_lottie(lottie_gif, height=280, key="data")
        

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=0)
    with col2:
        st_lottie(git_lottie, height=70,width=70, key="git", speed=0)
    with col3:
        st_lottie(github_lottie,height=70,width=70, key="github", speed=0)
    with col4:
        st_lottie(js_lottie,height=70,width=70, key="javascript", speed=1)
  
    
    with col1:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    with col2:
        st.subheader("Portfolio")
        # Embedding the links as images
        st.write("Check out my portfolio on:")
        st.markdown("[![Foo](data:image/png;base64,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)](https://palmetto.notion.site/The-Epting-Maker-s-Studio-0ea2942922a24ab3b7cd9a78774bd3d1?pvs=4)")
    with col3:
        st.subheader("Linkedin")
        st.write("Connect with me on:")
        st.markdown("[![Foo](data:image/png;base64,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)](https://www.linkedin.com/in/qepting)")
    with col4:
        st.subheader("Github")
        st.write("Or check out my code:")
        st.markdown("[![Foo](data:image/png;base64,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)](https://github.com/qepting91)")
