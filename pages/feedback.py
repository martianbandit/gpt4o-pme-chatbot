import streamlit as st

st.title("Feedback")
st.write("Leave your feedback here.")
st.text_input(placeholder="entrer vos commentaires ici...")
st.slider("Évaluez notre chatbot:", 1, 5, 3)
if st.button("Envoyer"):
    st.success("Votre feedback es très apprécié!")
