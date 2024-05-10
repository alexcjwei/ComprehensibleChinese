import streamlit as st
from constants import CHINESE_LEVELS, CHARACTER_TYPES
from chain import convert_chain

st.title("Comprehensible Chinese App")


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
    text = st.text_area("Enter text:", "我的中文不太好")
    chinese_level = st.select_slider("Chinese level", options=CHINESE_LEVELS)
    chinese_character_type = st.selectbox("Character type", options=CHARACTER_TYPES)
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text, chinese_character_type, chinese_level)
