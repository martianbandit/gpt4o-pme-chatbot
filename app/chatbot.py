import streamlit as st
import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_gpt4_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def chatbot_interface():
    st.header("Chatbot")
    user_input = st.text_input("Posez votre question :")
    if st.button("Envoyer"):
        response = get_gpt4_response(user_input)
        st.text_area("Réponse du chatbot", response, height=200)

