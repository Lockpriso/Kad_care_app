import streamlit

#displaying the image on streamlit app



streamlit.title('Kadige Care')
streamlit.header('Your health. Our passion.')
streamlit.subheader('Care That Lasts a Lifetime!')

col1, col2, col3 = streamlit.columns(3)

with col1:
   streamlit.header("About us")
   streamlit.image("https://static.streamlit.io/examples/cat.jpg")

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


