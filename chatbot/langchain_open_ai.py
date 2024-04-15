import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

llm.invoke("how can langsmith help with testing?")
