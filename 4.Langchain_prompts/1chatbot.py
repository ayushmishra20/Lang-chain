import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

st.title("Chatbot")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_version="v1beta"
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant")
    ]


for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

user_input = st.chat_input("You:")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    result = model.invoke(st.session_state.chat_history)
    
    st.chat_message("assistant").write(result.content)
    st.session_state.chat_history.append(AIMessage(content=result.content))