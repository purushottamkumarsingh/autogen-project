import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResarchAgent
from data_loader import DataLoader
load_dotenv()
print("i love you maa")
print("i love you Anjali")
#streamlit UI title
st.title("virtual Resarch Assistant")
#retrive the API from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")
##check the api key is set,else stop the execution
if not groq_api_key:
  st.error("GROQ_API_KEY is missing please the environment variables")

 #intialize the AI agents for the summarization
agents =ResarchAgent(groq_api_key)
##initalize the data loader for fetching resarch papers
data_loader =DataLoader()

##input field for the user to enter a resarch topic
query = st.text_input("enter the resarch topic")