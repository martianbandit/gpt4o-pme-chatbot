import streamlit as st

def login(username, password):
    # Vous pouvez ajouter votre logique d'authentification ici
    if username == "admin" and password == "password":
        st.session_state['logged_in'] = True

def check_login_status():
    return st.session_state.get('logged_in', False)

