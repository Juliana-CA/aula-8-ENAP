import streamlit as st
import pandas as pd
st.title('LOCALIZAÇÃO DAS COMUNIDADES QUILOMBOLAS - 2022')
dfq = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
dfq.drop(columns=['Unnamed: 0'], inplace=True)
lista = ['Lat_d', 'Long_d']
dfq[lista] = dfq[lista].apply(pd.to_numeric, errors='coerce')
dfq.info()
estados = dfq['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Selecione o estado',
     estados)
dadosFiltrados = dfq[dfq['NM_UF'] == estadoFiltro]
