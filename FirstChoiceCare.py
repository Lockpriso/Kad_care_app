import streamlit

#displaying the image on streamlit app



streamlit.title('Kadige Care')
streamlit.header('Your health. Our passion.')
streamlit.subheader('Care That Lasts a Lifetime!')

st.sidebar.title("Órbitas em Relatividade")
pagina_selecionada = streamlit.sidebar.selectbox("Selecione um tipo de órbita", ['Óbita de corpos celestes', 'Órbita de raios de luz'])
if pagina_selecionada == "Óbita de corpos celestes":
    streamlit.title("Particula massiva orbitando um buraco negro com a massa do Sol")
    streamlit.write("E se, de repente, o Sol se transformasse em um buraco negro?")
    streamlit.write("Para isso, toda sua massa, de 2 $\cdot$ 10$^{30}$ kg (hoje espalhada numa esfera com cerca de  700.000 km de raio), deveria ser comprimida numa região com raio de cerca de  3  km.")
   
