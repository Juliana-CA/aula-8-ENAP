import streamlit as st
import pandas as pd
st.title('LOCALIZAÇÃO DAS COMUNIDADES QUILOMBOLAS - 2022')
dfq = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
dfq.drop(columns=['Unnamed: 0'], inplace=True)
lista = ['Lat_d', 'Long_d']
dfq[lista] = dfq[lista].apply(pd.to_numeric, errors='coerce')
estados = dfq['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Selecione o estado',
    sorted(estados))
dadosFiltrados = dfq[dfq['NM_UF'] == estadoFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")
st.write('Comunidades Quilombolas por estado')
st.bar_chart(dfq['NM_UF'].value_counts())
st.write('Municipios com maior número de comunidades quilombolas')
st.bar_chart(dfq['NM_MUNIC'].value_counts()[:10])

qtdeMunicipios = len(dfq['NM_MUNIC'].unique())
st.write("Existem " + str(qtdeMunicipios) + " municípios com comunidades quilombolas")

qtdeComunidades = len(dfq['NM_AGLOM'].unique())
st.write("Nestes " +str(qtdeMunicipios) + " existem " + str(qtdeComunidades) + " comunidades quilombolas")

st.header('Número de comunidades por estado')
st.bar_chart(dfq['NM_UF'].value_counts())
