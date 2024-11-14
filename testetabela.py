import streamlit as st
import pandas as pd
df=pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [5200,6300,5000]
})
st.write("Criando uma tabela")
st.write(df)

opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
    options=["Selecione..."] + df['nomeServidor'].tolist()
)
