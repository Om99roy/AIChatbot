#import os
import streamlit as st
from api import gemini_key
from langchain_google_genai import ChatGoogleGenerativeAI

# Creating a model and the paramenter as well
model = ChatGoogleGenerativeAI(
    model = 'gemini-1.5-flash',
    api_key= gemini_key,
    verbose=False,
    temperature=0.8
)

st.title('Welcome to Langchain Generative AI')
input_text = st.text_area('Type here: ')

if st.button('Chat'):
    #st.write(model.invoke(input_text))
    #st.write(response)
    response = model.invoke(input_text)
    st.write(response.content)
