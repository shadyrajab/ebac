import streamlit as st
import pandas as pd


st.set_page_config(page_title='Exercício EBAC', layout='centered', page_icon='ebac-logo.png', initial_sidebar_state="expanded", menu_items= {
    'Get help': 'https://github.com/shadyrajab',
    'Report a bug': 'https://linkedin.com/in/shadyrajaab'
})

df = pd.read_csv('SINASC_RO_2019.csv', index_col=[0])

st.image('ebac-logo.png', width=100)
st.title('Exercício EBAC')
st.write('-----------------')
color = st.color_picker('Selecione a cor de fundo desejada')
st.markdown(f"""<style> 
        .main {{background: {color}}}<style>
        .css-1kyxreq e115fcil2 {{position: center}}"""
        ,unsafe_allow_html=True
    )
filtro = st.selectbox(label='# Selecione um filtro para a tabela', options=['Nenhum'] + list(df.columns))
filtro2 = st.selectbox(label='# Filtrar por nome de município', options=['Nenhum'] + list(df['munResNome'].unique()))
condicao = st.checkbox(label='Transformar dados categóricos em dummies')
file = st.file_uploader('Forneça a base de dados desejada')

if file:
    df = file

if condicao:
    df = pd.get_dummies(df)

if filtro != 'Nenhum' and filtro2 != 'Nenhum':
    df = df.set_index(filtro)
    table = st.dataframe(df[df['munResNome'] == filtro2])
elif filtro != 'Nenhum':
    df = df.set_index(filtro)
    table = st.dataframe(df)
elif filtro2 != 'Nenhum':
    table = st.dataframe(df[df['munResNome'] == filtro2])
else:
    table = st.dataframe(df)

st.video('devil-eyes.mp4')

st.markdown("""```python
import streamlit as st
import pandas as pd


st.set_page_config(page_title='Exercício EBAC', layout='centered', page_icon='ebac-logo.png', initial_sidebar_state="expanded", menu_items= {
    'Get help': 'https://github.com/shadyrajab',
    'Report a bug': 'https://linkedin.com/in/shadyrajaab'
})

df = pd.read_csv('SINASC_RO_2019.csv', index_col=[0])

st.image('ebac-logo.png', width=100)
st.title('Exercício EBAC')
st.write('-----------------')
color = st.color_picker('Selecione a cor de fundo desejada')
st.markdown(f''''<style> 
        .main {{background: {color}}}<style>
        .css-1kyxreq e115fcil2 {{position: center}}'''
        ,unsafe_allow_html=True
    )
filtro = st.selectbox(label='# Selecione um filtro para a tabela', options=['Nenhum'] + list(df.columns))
condicao = st.checkbox(label='Transformar dados categóricos em dummies')
file = st.file_uploader('Forneça a base de dados desejada')

if file:
    df = file

if condicao:
    df = pd.get_dummies(df)

if filtro != 'Nenhum':
    filtered_df = df.set_index(filtro)
    table = st.dataframe(filtered_df)
else:
    table = st.dataframe(df)

st.video('devil-eyes.mp4')
st.image('brazil.png', width=400)```""")

st.image('brazil.png', width=700)