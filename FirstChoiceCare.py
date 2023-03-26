import streamlit

streamlit.title('Kadige Care')
streamlit.header('Your health. Our passion.')
streamlit.subheader('Care That Lasts a Lifetime!')

st.sidebar.title("Órbitas em Relatividade")
pagina_selecionada = st.sidebar.selectbox("Selecione um tipo de órbita", ['Óbita de corpos celestes', 'Órbita de raios de luz'])
if pagina_selecionada == "Óbita de corpos celestes":
    st.title("Particula massiva orbitando um buraco negro com a massa do Sol")
    st.write("E se, de repente, o Sol se transformasse em um buraco negro?")
    st.write("Para isso, toda sua massa, de 2 $\cdot$ 10$^{30}$ kg (hoje espalhada numa esfera com cerca de  700.000 km de raio), deveria ser comprimida numa região com raio de cerca de  3  km.")
    # IMAGE HERE AFTER TEXT
    st.subheader("Escolha o valor da posição inicial (em km):")  
    x0 = st.slider("Escolha entre 3km e 50km",min_value=3.0, max_value=50.0, step = 0.1)  
    image = Image.open('C:\Users\PPR\Downloads/Image1.jpeg')
    st.image(image, caption='Escolha entre 3km e 50km')
