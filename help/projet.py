import streamlit as st
from alix import assistante



# Ajout d'un titre
st.title('ALIX')
st.header('Assistante Locale Intelligent eXtended')
st.subheader('Votre Assistance à porter de main')


# Affichage du DataFrame
st.write(df)

# Ajout d'un bouton
if st.button('Cliquez-moi'):
    st.write('Vous avez cliqué sur le bouton !')






