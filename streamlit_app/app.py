import streamlit as st
import json
from services.user_service import register_user, login_user
from services.ingestion_service import ingest_data
from services.file_service import extract_text_from_pdf, save_uploaded_file
from services.data_storage import load_data
from services.chatbot_service import generate_prompt, get_chatbot_response
from services.feedback_interface import submit_feedback, get_feedback

st.set_page_config(page_title="Assistant IA", layout="wide")

# Charger les informations de l'entreprise
company_data = load_data('company_data.json')

# Onglets pour les différentes sections
tabs = ["Accueil", "Inscription", "Connexion"]
if 'user' in st.session_state:
    if st.session_state['user'].get('is_admin'):
        tabs.extend(["Ingestion de données", "Calculs et Prix", "Gestion des Fichiers (Admin)", "Chatbot", "Feedback"])
    else:
        tabs.extend(["Ingestion de données", "Calculs et Prix", "Chatbot", "Feedback"])

selected_tab = st.sidebar.selectbox("Navigation", tabs)

# Onglet Accueil
if selected_tab == "Accueil":
    st.title("Bienvenue sur l'Assistant IA du Spécialiste du Vrac")
    st.write("""
        Cette application vous aide à déterminer les quantités de matériaux nécessaires pour vos projets de jardinage.
        Vous pouvez vous inscrire ou vous connecter pour accéder à des fonctionnalités avancées.
    """)

# Onglet Inscription
elif selected_tab == "Inscription":
    st.header("Inscription")
    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    is_admin = st.checkbox("Inscription en tant qu'administrateur")
    if st.button("S'inscrire"):
        response = register_user(email, password, is_admin)
        if 'error' in response:
            st.error(response['error']['message'])
        else:
            st.success("Inscription réussie !")

# Onglet Connexion
elif selected_tab == "Connexion":
    st.header("Connexion")
    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        response = login_user(email, password)
        if 'error' in response:
            st.error(response['error']['message'])
        else:
            st.session_state['user'] = response['user']
            st.success("Connexion réussie !")

# Vérification si l'utilisateur est connecté
if 'user' in st.session_state:
    # Onglet Ingestion de données
    if selected_tab == "Ingestion de données":
        st.header("Ingestion de données")
        data = st.text_area("Données JSON")
        if st.button("Ingérer"):
            try:
                data_dict = json.loads(data)
                user_id = st.session_state['user']['id']
                response = ingest_data(user_id, data_dict)
                st.success("Données ingérées avec succès !")
            except json.JSONDecodeError:
                st.error("Format JSON invalide")

    # Onglet Calculs et Prix
    elif selected_tab == "Calculs et Prix":
        st.header("Calcul des Quantités et des Prix")

        surface = st.number_input("Surface en mètres carrés")
        profondeur = st.number_input("Profondeur en centimètres")
        type_materiau = st.selectbox("Type de matériau", ["Terre", Sable, Paillis"])

        if st.button("Calculer"):
            volume = surface * profondeur / 100  # Convertir en mètres cubes
            # Ajoutez ici des calculs spécifiques pour convertir en verges ou en tonnes
            st.write(f"Volume nécessaire : {volume} mètres cubes")

            prix_par_unite = 50  # Exemple de prix par mètre cube
            frais_livraison = 30  # Exemple de frais de livraison
            taxe = 0.15  # Exemple de taux de taxe

            total = volume * prix_par_unite + frais_livraison + (volume * prix_par_unite * taxe)
            st.write(f"Prix total : {total} $")

    # Onglet Gestion des Fichiers (Admin)
    elif selected_tab == "Gestion des Fichiers (Admin)":
        if st.session_state['user']['is_admin']:
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
        else:
            st.warning("Vous n'avez pas les autorisations nécessaires pour accéder à cette section.")

    # Onglet Chatbot
    elif selected_tab == "Chatbot":
        st.header("Chatbot")

        question = st.text_area("Posez une question au chatbot")
        if st.button("Envoyer"):
            # Exemple de fichier PDF contenant des informations
            pdf_file_path = 'path/to/your/pdf_file.pdf'
            extracted_info = extract_text_from_pdf(pdf_file_path)
            prompt = generate_prompt(question, extracted_info, company_data)
            response = get_chatbot_response(prompt)
            st.write(f"Réponse du Chatbot : {response}")

    # Onglet Feedback
    elif selected_tab == "Feedback":
        st.header("Feedback")

        rating = st.slider("Notez notre application", 1, 5)
        comments = st.text_area("Commentaires")
        if st.button("Soumettre le feedback"):
            user_id = st.session_state['user']['id']
            response = submit_feedback(user_id, rating, comments)
            if 'error' in response:
                st.error("Erreur lors de la soumission du feedback")
            else:
                st.success("Merci pour votre feedback !")

        st.header("Feedback des utilisateurs")
        feedback_data = get_feedback()
        for feedback in feedback_data:
            st.write(f"Note : {feedback['rating']}")
            st.write(f"Commentaires : {feedback['comments']}")
            st.write("---")

# Si l'utilisateur n'est pas connecté, afficher uniquement les onglets Accueil, Inscription et Connexion
else:
    st.title("Bienvenue sur l'Assistant IA du Spécialiste du Vrac")
    st.write("""
        Veuillez vous inscrire ou vous connecter pour accéder aux fonctionnalités avancées de l'application.
    """)
