import pandas as pd
import plotly.express as px
import streamlit as st

     
car_data = pd.read_csv('vehicles_us.csv') # lendo os dados
st.header('Odometer data')
hist_button = st.button('Create histogram and scatter plot') # criar um botão
     
if hist_button: # se o botão for clicado
         # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
    fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

    fig_2 = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão

    st.plotly_chart(fig_2, use_container_width=True)
