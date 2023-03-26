import streamlit

#displaying the image on streamlit app



streamlit.title('🏤 👨‍⚕️ Kadige Care')
streamlit.header('Votre santé. Notre passion.')
streamlit.text('Des soins qui durent toute une vie !')
streamlit.subheader("♌A propos de nous")
streamlit.text("Bienvenue chez Kadige Care (KC)")
streamlit.markdown("Nous sommes une structure de santé communautaire qui vise à fournir des services médicaux de haute qualité à la population locale." 
                  "Notre hôpital est dédié à répondre aux besoins de santé des :blue[personnes vivant dans les zones rurales], qui ont souvent peu" 
                  "d'accès aux services médicaux essentiels.")
streamlit.markdown("Notre hôpital est plus qu'une simple installation médicale ; :blue[c'est une communauté]. Nous sommes engagés à travailler en étroite" 
                   "collaboration avec la communauté locale pour nous assurer que nos services sont adaptés à leurs besoins spécifiques. Nous croyons que"
                   "la participation communautaire est cruciale pour améliorer les résultats en matière de santé, et nous :blue[accueillons les commentaires de "
                   "nos patients et de leur famille.])
streamlit.text("Merci de considérer notre hôpital pour vos besoins de santé. Nous sommes impatients de vous servir," 
                   "vous et votre famille.")


# Using "with" notation
with streamlit.sidebar:
    add_radio = streamlit.radio(
        "Menu",
        ("A propos de nous", "Notre mission","nos valeurs", "Prenez rendez-vous", "Avez-vous des questions?")
    )


