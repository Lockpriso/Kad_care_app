import streamlit

#displaying the image on streamlit app



streamlit.title('🏤 👨‍⚕️ Kadige Care')
streamlit.header('Your health. Our passion. Care That Lasts a Lifetime!')

col1, col2, col3 = streamlit.columns(3)

with col1:
   streamlit.header("About us")
   streamlit.text("Bienvenue chez Kadige Care (KC)")
   streamlit.text("Nous sommes une structure de santé communautaire qui vise à fournir des services médicaux de haute qualité à la population locale." 
                  "Notre hôpital est dédié à répondre aux besoins de santé des personnes vivant dans les zones rurales, qui ont souvent peu" 
                  "d'accès aux services médicaux essentiels.")

with col2:
   streamlit.header("Our Mission")
   streamlit.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   streamlit.header("Our Values")
   streamlit.image("https://static.streamlit.io/examples/owl.jpg")


# Using "with" notation
with streamlit.sidebar:
    add_radio = streamlit.radio(
        "Contact us",
        ("Email", "Home phone", "Mobile phone")
    )


