import streamlit as st

option = st.sidebar.radio(options=["home", "speed_recontre", "chat"], label="choisissez votre mode !")

if option == "home":
    style="""{
    height : 300px;
    color : blue
    
    }"""

    st.html(f"<h3 style={style}>{open("bienvenue.txt", "r").read()}</h3>")

