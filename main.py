import streamlit as st
from sum1 import nltk_summarizer
from sum4 import generate_summary

st.title("Text summarixer")
menu = ["Home","Extractive","Abstractive"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
        st.subheader("Home")
        st.write("AI mini project")

elif choice == "Extractive":
        st.subheader("Extractive")
        input=st.text_area("Input text")
        if st.button("Generate"):
                st.write(nltk_summarizer(input))

elif choice == "Abstractive":
        st.subheader("Abstractive")
        input=st.text_area("Input text")
        mi = st.slider('minimum number of words', 40, 200, 25)
        ma = st.slider('maximum number of words', 40, 200, 25)
        if st.button("Generate"):

                st.write(generate_summary(input,mi,ma))


