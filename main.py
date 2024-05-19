import streamlit as st
from streamlit_app.authentication import login, check_login_status
from services.chatbot_services import chatbot_service
from services.feedback import feedback_interface
from services.metrics import metrics_interface

# Initialisation de l'état de session
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Interface de connexion
if not st.session_state['logged_in']:
    st.title("Connexion")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type='password')
    if st.button("Se connecter"):
        login(username, password)
        if st.session_state['logged_in']:
            st.success("Connexion réussie !")
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
else:
    st.title("Le Spécialiste du Vrac - Chatbot")
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Aller à", ["Chatbot", "Feedback", "Métriques"])

    if selection == "Chatbot":
        chatbot_interface()
    elif selection == "Feedback":
        feedback_interface()
    elif selection == "Métriques":
        metrics_interface()

