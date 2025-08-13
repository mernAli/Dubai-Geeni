from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import os 

load_dotenv(dotenv_path="D:\AI_BOOTCAMP\.env")
print("Loaded key:", os.getenv("OPENAI_API_KEY"))  # Debug
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

initial_message = [
        {"role" : "system" , "content" : "You ara a trip planner in Kerala and Dubai. You are an expert in Kerala and Dubai Tourism, locations, foods, events, hotels, etc. You are able to guide users to plan vacation to kerala. You should respond professionally. Your name is Dubai Genie, short name is DG. Response shouldn't exceed 200 words. Always ask question to the user and help them to plan the trip. Finally give a day wise itinerary. Deal with user professionally" },
        {
            "role" : "assistant",
            "content" : "Hello I am Dubai Genie from AliGPT, your expert trip planner. How can I help you? "
        }

]
# Function to get response from OpenAI LLM
def get_response_from_llm(messages):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)
    return completion.choices[0].message.content
#_____________________

if "messages" not in st.session_state:
    st.session_state.messages = initial_message

st.title("Dubai Trip Assistant App")

# Display previouse chat content

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_message = st.chat_input("Enter your message")

if user_message:
    new_message =  {
            "role" : "user",
            "content" : user_message
        }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
            st.markdown(new_message["content"])
    response = get_response_from_llm(st.session_state.messages)
    if response:
        response_message = {
             "role" : "assistant",
             "content" : response
        }
        st.session_state.messages.append(response_message)
        with st.chat_message(response_message["role"]):
            st.markdown(response_message["content"])