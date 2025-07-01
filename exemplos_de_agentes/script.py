import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
import time
from langchain.prompts import PromptTemplate


load_dotenv()

open_ai_key = os.getenv("OPEN_AI_KEY")

llm = OpenAI(api_key=open_ai_key, model_name="gpt-3.5-turbo-instruct")

prompt = PromptTemplate(
    input_variables=["creature"],
    template="Write a one-senteces bedtime story about a {creature}."
    
)

chain = prompt | llm

response = chain.invoke({"creature": "uvicorn"})

print(response)