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
    temperature=0.2
)

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

# LLM router setup
router_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a classifier that only replies with one of the following categories: 'math', 'philosophy', 'doctor', or 'default'."),
    ("human", "Which category does this question belong to?\n\nQuestion: {input}\n\nCategory:")
])
router_chain = router_prompt | llm | output_parser

# Streamlit UI
st.title("LangChain + Groq Smart Routed Chatbot")
input_text = st.text_input("Ask something:")

if input_text:
    route = router_chain.invoke({'input': input_text}).strip().lower()

    # Pick the chain based on route
    if route == "math":
        response = math_chain.invoke({'input': input_text})
    elif route == "philosophy":
        response = philosophy_chain.invoke({'input': input_text})
    elif route == "doctor":
        response = doctor_chain.invoke({'input': input_text})
    else:
        response = default_chain.invoke({'input': input_text})

    st.write(f"**({route.capitalize()} Expert)**: {response}")
