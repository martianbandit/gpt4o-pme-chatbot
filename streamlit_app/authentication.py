import streamlit as st

def login(email, password):
    response = login_user(email, password)
    if 'error' in response:
        st.error(response['error']['message'])
    else:
        st.session_state['user'] = response['user']
        st.success("Connexion réussie !")

def check_login_status():
    return 'user' in st.session_state
