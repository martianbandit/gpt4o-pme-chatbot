import streamlit as st

st.title("Feedback")
st.write("Leave your feedback here.")
st.slider("Rate the chatbot:", 1, 5, 3)
if st.button("Submit"):
    st.success("Thank you for your feedback!")
