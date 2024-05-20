import streamlit as st
from utils.auth import check_auth, login, logout

st.set_page_config(page_title="Le Spécialiste du Vrac", page_icon="🛒", layout="wide")

# Pages disponibles dans l'application
pages = {
    "Home": "pages/home.py",
    "Chatbot": "pages/chatbot.py",
    "Feedback": "pages/feedback.py",
    "Metrics": "pages/metrics.py"
}

# Authentification de l'utilisateur
if "username" not in st.session_state:
    st.session_state["username"] = None

if st.session_state["username"] is None:
    login()
else:
    logout()
    st.sidebar.title(f"Welcome, {st.session_state['username']}")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    st.experimental_rerun()

    with open(pages[selection]) as f:
        exec(f.read())
