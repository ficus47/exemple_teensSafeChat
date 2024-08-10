import streamlit as st

style="""{
    height:300px
    
}"""

st.html(f"<h3 style={style}>{open("bienvenue.txt", "r").read()}</h3>")

option = st.sidebar.radio(options=["home", "speed_recontre", "chat"], label="choisissez votre mode !")
