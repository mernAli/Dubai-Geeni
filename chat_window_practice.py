import streamlit as st
st.title("AliGPT - Chat Window")
with st.chat_message("ai"):
    st.markdown("Hello, I am an AI assistant, How can I help you?")
    
with st.chat_message("human"):
    st.markdown("I am planning a vacation trip to Dubhai")

message = st.chat_input("Enter your message: ")
if message:
    with st.chat_message("human"):
        st.markdown(message)