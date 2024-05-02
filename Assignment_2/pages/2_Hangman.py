## Notes

import streamlit as st

st.title("Hangman")

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("Next"):
    st.session_state.count += 1

st.image(f"hangman_{st.session_state.count}.png")