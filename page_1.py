import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# .env 파일의 OPENAI_API_KEY를 환경변수로 불러옴
load_dotenv()


# 페이지가 다시 실행될 때마다 모델을 새로 만들지 않도록 캐시
@st.cache_resource
def get_model():
    return init_chat_model("gpt-5.4-mini", model_provider="openai")


st.title("우리 회사 챗봇")

if not os.getenv("OPENAI_API_KEY"):
    st.error("OPENAI_API_KEY가 없습니다. 프로젝트 폴더의 .env 파일에 키를 넣어주세요.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("여기에 입력하시오.")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    try:
        # 이전 대화까지 함께 보내서 맥락을 기억하게 함
        response = get_model().invoke(st.session_state.messages)
        st.session_state.messages.append({"role": "ai", "content": response.content})
    except Exception as e:
        st.session_state.messages.pop()
        st.error(f"답변을 받지 못했습니다: {e}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
