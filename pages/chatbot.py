import streamlit as st

st.title("Chatbot")
st.write("This is where the chatbot interface for Le Spécialiste du Vrac will be.")

# Sidebar pour les instructions et icônes
st.sidebar.title("Instructions")
st.sidebar.write("Here you can configure the instructions for the GPT model.")

# Section des instructions
instructions = st.sidebar.text_area("GPT Instructions", "Default instructions here...")

# Ajout d'icônes et explications
st.sidebar.write("### Icons")
st.sidebar.write("🔍 Search icon for initiating searches.")
st.sidebar.write("💬 Chat icon for starting conversations.")

# Interface du chatbot
st.write("Configure GPT instructions here:")
st.write(instructions)
