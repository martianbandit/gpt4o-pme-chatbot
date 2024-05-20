import streamlit as st

def check_auth(username, password):
    # Ajouter la logique d'authentification ici
    return username == "user" and password == "password"

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_auth(username, password):
            st.session_state["username"] = username
            st.experimental_rerun()
        else:
            st.error("Incorrect username or password")

def logout():
    if st.sidebar.button("Logout"):
        st.session_state["username"] = None
        st.experimental_rerun()
