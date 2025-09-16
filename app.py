from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set keys
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Set up LLM
llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0.5
)

# Output parser
output_parser = StrOutputParser()

# Expert prompts
math_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a math professor. Answer only math-related questions with clear reasoning."),
    ("human", "{input}"),
])

philosophy_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a philosopher. Answer in a deep, thoughtful, and reflective tone."),
    ("human", "{input}"),
])

doctor_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a medical doctor. Only answer health-related questions with accurate and responsible guidance."),
    ("human", "{input}"),
])

default_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the user's questions to the best of your ability."),
    ("human", "{input}"),
])

# Chains
math_chain = math_prompt | llm | output_parser
philosophy_chain = philosophy_prompt | llm | output_parser
doctor_chain = doctor_prompt | llm | output_parser
default_chain = default_prompt | llm | output_parser

# Router function
def route_input(input_text):
    lower = input_text.lower()
    if any(word in lower for word in ["integral", "algebra", "math", "equation", "geometry"]):
        return "math"
    elif any(word in lower for word in ["meaning", "life", "ethics", "existence", "truth", "philosophy"]):
        return "philosophy"
    elif any(word in lower for word in ["fever", "pain", "headache", "health", "doctor", "medicine", "symptom"]):
        return "doctor"
    else:
        return "default"

# Streamlit UI
st.title("LangChain + Groq Routed Chatbot")
input_text = st.text_input("Ask something:")

if input_text:
    route = route_input(input_text)
    
    if route == "math":
        response = math_chain.invoke({'input': input_text})
    elif route == "philosophy":
        response = philosophy_chain.invoke({'input': input_text})
    elif route == "doctor":
        response = doctor_chain.invoke({'input': input_text})
    else:
        response = default_chain.invoke({'input': input_text})

    st.write(f"**({route.capitalize()} Expert)**: {response}")
