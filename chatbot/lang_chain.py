from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)


## Steamlit Framework
st.title('Langchain Demo with OpenAi api')
input_text=st.text_input("Search the topic you want")

## OpenAi Llm
llm=ChatOpenAI()
output_parser=StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))



