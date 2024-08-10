import streamlit as st

st.write(open("bienvenue.txt", "r").read())

option = st.sidebar.radio(options=["home", "speed_recontre", "chat"], label="choisissez votre mode !")
