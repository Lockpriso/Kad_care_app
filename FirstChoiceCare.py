import streamlit

#displaying the image on streamlit app



streamlit.title('🏤 👨‍⚕️ Kadige Care')
streamlit.header('Votre santé. Notre passion. Des soins qui durent toute une vie !')


   streamlit.header("A propos de nous")
   streamlit.text("Bienvenue chez Kadige Care (KC)")
   streamlit.text("Nous sommes une structure de santé communautaire qui vise à fournir des services médicaux de haute qualité à la population locale." 
                  "Notre hôpital est dédié à répondre aux besoins de santé des personnes vivant dans les zones rurales, qui ont souvent peu" 
                  "d'accès aux services médicaux essentiels.")


# Using "with" notation
with streamlit.sidebar:
    add_radio = streamlit.radio(
        "Contact us",
        ("Email", "Home phone", "Mobile phone")
    )


