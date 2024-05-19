import streamlit as st
from services.file_service import save_uploaded_file, extract_text_from_pdf

st.set_page_config(page_title="Admin - Assistant IA", layout="wide")

st.header("Téléchargement des Fichiers (Admin)")

uploaded_files = st.file_uploader("Choisir des fichiers PDF ou images", accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = save_uploaded_file(uploaded_file)
        st.write(f"Fichier téléchargé : {uploaded_file.name}")
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(file_path)
            st.write(text)
        else:
            st.image(file_path)

