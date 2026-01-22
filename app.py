import streamlit as st
st.title("Survey")
st.text_input("Please enter your name: ")
st.number_input("Please enter your age: ")
subject=st.selectbox("Please select your favorite subject: ", ["Maths", "English", "German", "PE"])
if st.button("PRESS MEEEEEE"):
  st.success("WOOOOOOOOOO")
