import streamlit as st
import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import matplotlib.dates as mdates


st.markdown('***')
st.title('Analytics app')
st.markdown('***')

st.sidebar.markdown('Impacto del COVID-19 en el mercado financiero y en la lista índice S&P500')
st.sidebar.markdown('***')
st.sidebar.markdown('Análisis de riesgo')
st.sidebar.markdown('***')
st.sidebar.markdown('Análisis de crecimiento')
st.markdown('''
 Es cierto que la pandemia del COVID-19 tuvo un impacto significativo en los mercados financieros en todo el mundo,
incluyendo la lista índice S&P500. En particular, a principios de 2020, el mercado sufrió una gran caída
en el precio de las acciones debido a la incertidumbre causada por la pandemia
''')
st.markdown('''
 Si comparamos el comportamiento del índice S&P500 en los años previos al COVID-19 con el comportamiento 
durante la pandemia, podemos observar una diferencia significativa. Antes de la pandemia, 
el índice S&P500 mostraba una tendencia alcista estable, con fluctuaciones normales en el corto plazo.
 Sin embargo, a partir de marzo de 2020, el índice experimentó una fuerte caída, 
seguida de una recuperación rápida y volátil.
''')
st.markdown('***')

# Descargar datos históricos de Apple y el S&P 500
apple = yf.download("AAPL", start="2000-01-01")
sp500 = yf.download("^GSPC", start="2000-01-01")

# Fusionar los datos de Apple y el S&P 500 en un solo DataFrame
data = pd.merge(apple['Close'], sp500['Close'], left_index=True, right_index=True, suffixes=('_apple', '_sp500'))

# Calcular la desviación estándar de los precios de cierre de Apple en relación al S&P 500
std_dev = data['Close_apple'].std() / data['Close_sp500'].std()

# Graficar los precios de cierre de Apple y el S&P 500 usando Matplotlib
fig, ax = plt.subplots()
ax.plot(data['Close_apple'], label='Apple')
ax.plot(data['Close_sp500'], label='S&P 500')
ax.legend()
st.pyplot(fig)

# Imprimir la desviación estándar de Apple en relación al S&P 500
st.write(f"La desviación estándar de los precios de cierre de Apple en relación al S&P 500 es {std_dev:.2f}")









st.markdown('***')
st.markdown('contacto')
