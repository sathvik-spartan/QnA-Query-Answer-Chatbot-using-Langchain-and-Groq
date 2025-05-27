import os
import langchain
from langchain.chains.question_answering.map_rerank_prompt import output_parser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

os.environ["groq_api_key"] = os.getenv("GROQ_API_KEY")
os.environ["langchain_api_key"] = os.getenv("LANGCHAIN_API_KEY")

# Defining Prompts
prompt = ChatPromptTemplate.from_messages([
    ("system","You are a good assistant"),
    ("user","question: {question}")
])

# Generate Responses
def generate_response(question, engine, temperature, max_token):
    llm = ChatGroq(model = engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question": question})
    return answer

#Streamlit stuff
st.title("QnA Chatbot")
engine = st.sidebar.selectbox("select model",["gemma2-9b-it","meta-llama/Llama-Guard-4-12B","llama-3.3-70b-versatile","llama-3.1-8b-instant"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_token = st.sidebar.slider("Max tokens", min_value=100, max_value=500)

# User 🙏
st.write("Ask your Query/Queries")
user_input = st.text_input("Enter your query")
if user_input:
    response = generate_response(user_input, engine, temperature, max_token)
    st.write(response)
else:
    st.write("Please enter a query.")
