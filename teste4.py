import streamlit as st
import pandas as pd
st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
nota=st.select_slider('Nota de 0 a 100', range(0,101,10))
st.write(nota)
# criando elementos gráficos
'''Informar como colher os dados através de variáveis'''
x = st.checkbox('Sim')
st.write(x)

# fazer o mesmo com alguns dos comandos abaixo
st.title(x)
st.button('Clique')
st.radio('Selecione seu gênero',['Masculino','Feminino'])
st.selectbox('Selecione seu gênero',['Masculino','Feminino'])
st.multiselect('Escolha um departamento',['DCS', 'DE', 'DIR'])
st.select_slider('Selecione uma resposta', ['Ruim', 'Bom', 'Excelente'])
st.slider('Selecione um número', 0,50)
st.number_input('Selecione um número', 0,10)
st.text_input('Endereço de e-mail')
st.date_input('Data de viagem')
st.time_input('Tempo de escola')
st.text_area('Descrição')
st.file_uploader('Atualize uma foto')
st.color_picker('Escolha sua cor favorita')

# mensagens de status
st.success("Você conseguiu!")
st.error("Erro!")
st.warning("Advertência")
st.info("Esta é uma informação")

#inserindo dataframe
df=pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [5200,6300,5000]
})
st.write("Criando uma tabela")
st.write(df)
