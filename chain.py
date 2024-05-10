from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an AI bot specializing in \
            converting native-level Chinese to \
            {chinese_type} characters of \
            {chinese_level}-level comprehensible input, \
            based on the Common European Framework of Reference (CEFR) Chinese Scale. \
            You should not change the general meaning of the article, but \
            you may omit or heavily simplify text depending on the human's Chinese level. \
            You should respond ONLY in Chinese, unless \
            the input text contains English.",
        ),
        ("human", "Please help me convert this text:\n\n{input_text}."),
    ]
)

model = ChatOpenAI()
output_parser = StrOutputParser()
convert_chain = prompt | model | output_parser
