import streamlit as st
from langchain.llms import OpenAI
from helper import get_openai_api_key
from constants import CHINESE_LEVELS, CHARACTER_TYPES
from chain import convert_chain

st.title("Comprehensible Chinese App")

openai_api_key = get_openai_api_key()


def generate_response(input_text, chinese_type, chinese_level):
    output_text = convert_chain.invoke(
        {
            "input_text": input_text,
            "chinese_type": chinese_type,
            "chinese_level": chinese_level,
        }
    )
    st.info(output_text)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:", "What are 3 key advice for learning how to code?"
    )
    chinese_level = st.select_slider("Chinese level", options=CHINESE_LEVELS)
    chinese_character_type = st.selectbox("Character type", options=CHARACTER_TYPES)
    submitted = st.form_submit_button("Submit", disabled=not openai_api_key)
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text, chinese_character_type, chinese_level)
