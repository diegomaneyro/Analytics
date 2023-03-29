import streamlit as st
import os
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from datetime import datetime, timedelta
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Analytics-app')
st.markdown('***')
st.sidebar.markdown('* Impacto del COVID-19 en el mercado financiero y en la lista índice S&P500')
st.sidebar.markdown('* EDA Indice SP-500')
st.sidebar.markdown('* Análisis de riesgo')
st.sidebar.markdown('* Análisis de crecimiento')
st.sidebar.markdown('* Recomendación de inversion: \n Empresa y dia')

st.markdown('''
>La pandemia del COVID-19 tuvo un impacto significativo en los mercados financieros en todo el mundo,
incluyendo la lista índice S&P500. En particular, a principios de 2020, el mercado sufrió una gran caída
en el precio de las acciones debido a la incertidumbre causada por la pandemia.
''')
st.markdown('''
>Si comparamos el comportamiento del índice S&P500 en los años previos al COVID-19 con el comportamiento 
durante la pandemia, podemos observar una diferencia significativa. Antes de la pandemia, 
el índice S&P500 mostraba una tendencia alcista estable, con fluctuaciones normales en el corto plazo.
 Sin embargo, a partir de marzo de 2020, el índice experimentó una fuerte caída, 
seguida de una recuperación rápida y volátil.
''')
st.markdown('***')
st.subheader('Análisis del Indice SP-500')

# ingestar datos desde csv en un dataframe de pandas
sp500_data = pd.read_csv('sp500_historical_data.csv')
# crear un check para seleccionar filas o columnas y luego se visualiza los datos del csv
st.subheader('Información sp500: datos históricos posterior al año 2000') 
if st.checkbox('Mostrar SP-500 Historico'):
    st.dataframe(sp500_data)
# Visualizacion inicial de los primeros registros
st.dataframe(sp500_data.describe())

st.markdown('***')
sp500_empresas = pd.read_csv('sp500_empresas.csv')
st.subheader('Información de Microsoft, Apple, Google, Amazon')
if st.checkbox('Mostrar SP-500 Empresas'):
    st.dataframe(sp500_empresas)
st.dataframe(sp500_empresas.describe())
st.markdown('***')
