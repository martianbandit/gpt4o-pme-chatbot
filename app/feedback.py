import streamlit as st
from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def feedback_interface():
    st.header("Feedback")
    rating = st.slider("Notez notre chatbot", 1, 5)
    feedback = st.text_area("Votre feedback")
    if st.button("Envoyer le feedback"):
        data = {"rating": rating, "feedback": feedback}
        supabase.table('feedback').insert(data).execute()
        st.success("Merci pour votre feedback !")

