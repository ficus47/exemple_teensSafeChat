import streamlit as st

option = st.sidebar.radio(options=["home", "speed_rencontre", "chat"], label="choisissez votre mode !")

if option == "home":
    st.write("""Bienvenue sur TeenSafeChat, votre site de rencontres sécurisé pour adolescents, protégé par l'IA !\n

                                La sécurité de nos utilisateurs et la protection de leurs données sont nos priorités absolues. C'est pourquoi nous avons développé AImage, notre IA avancée capable de vérifier l'âge des utilisateurs à partir d'une simple photo. De plus, nous travaillons activement sur une IA dédiée à la modération des discussions et des profils, pour garantir un environnement sûr et respectueux.
                                
                                Nous vous souhaitons une expérience agréable et de belles rencontres !\n
                                
                                Pour toute réclamation, question ou demande d'assistance, n'hésitez pas à nous contacter à l'adresse suivante : [email à venir].\n""")

elif option == "speed_rencontre":
    try:
        if st.session_state["first"] != "yes":
            column1, column2 = st.columns([2,1])


        column1.image("images.jpg")
        column2.write("""
                        sex : feminin\n
                        age : 8 mois\n
                        autre : trop chou\n
                        orientation sexuel : aime tout le monde\n
                        """)
        st.write("""**description**:
                 je suis une petite chatte trés mignone qui ne demande que de l'amours""")
        st.button("prochaine proposition")
        
    except Exception:
        st.session_state["first"] = "no"

        st.balloons()
        
        st.write("""**Bienvenue sur la section Speed-Date de TeenSafeChat !**\n
                 
                    Dans cette section, vous pourrez découvrir des profils qui vous seront proposés en fonction de vos informations (âge, orientation sexuelle, etc.). Vous aurez la possibilité de les contacter ou simplement de passer au profil suivant !\n                       
                    
                    Pour vous offrir une meilleure expérience, nous utilisons votre historique de navigation. Ne vous inquiétez pas, ces informations ne seront utilisées que pour améliorer les suggestions qui vous seront faites.\n                        
                    
                    Nous basons nos recommandations sur les 50 derniers profils que vous avez consultés. Cependant, en souscrivant à notre forfait premium à seulement 0,50 € par mois, vous pourrez doubler le nombre de profils pris en compte. En plus, ce forfait vous donne accès à un algorithme de recommandation amélioré (et qui sait, peut-être bientôt basé sur l'IA 😉).\n
                    """)
        st.button("passer au speed rencontre")
    
elif option == "chat":
    # Initialisation de la session pour stocker l'historique des messages
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Fonction pour ajouter un nouveau message
    def add_message():
        if st.session_state['user_input']:
            st.session_state['messages'].append({"user": "Vous", "text": st.session_state['user_input']})
            st.session_state['user_input'] = ''  # Réinitialiser l'entrée utilisateur
            if len(st.session_state['messages']) > 50:
                st.session_state['messages'] = st.session_state['messages'][-50:]

    # Titre de l'application
    st.title("Système de Chat Simple")

    # Afficher l'historique des messages
    st.subheader("Historique des messages")
    for msg in st.session_state['messages']:
        st.write(f"{msg['user']}: {msg['text']}")

    # Entrée utilisateur
    st.text_input("Tapez votre message ici:", key='user_input', on_change=add_message)
