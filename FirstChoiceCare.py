import streamlit

#displaying the image on streamlit app



streamlit.title('Kadige Care')
streamlit.header('Your health. Our passion.')
streamlit.subheader('Care That Lasts a Lifetime!')

# Using object notation
add_selectbox = streamlit.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with streamlit.sidebar:
    add_radio = streamlit.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


