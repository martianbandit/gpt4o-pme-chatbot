import streamlit as st
from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def metrics_interface():
    st.header("Métriques")
    if st.button("Extraire les métriques"):
        feedback_data = supabase.table('feedback').select('*').execute()
        st.write("Métriques extraites : ", feedback_data.data)

