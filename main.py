import streamlit as st
from sum1 import nltk_summarizer

st.title("Text summarixer")
menu = ["Home","TextS1","TextS2"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
        st.subheader("Home")

elif choice == "TextS1":
        st.subheader("TextS1")
        input=st.text_input("Input text")
        if st.button("Generate"):
                st.write(nltk_summarizer(input))

elif choice == "TextS2":
        st.subheader("TextS2")
