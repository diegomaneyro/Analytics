
## Autor: Diego Maneyro

- [Linkedin](https://www.linkedin.com/in/diego-maneyro/)


# Análisis de Indice SP500 Mercado Bursatil

<h1 align=center> Analytics </h1>
</br>
<p align="center">
<img src="https://github.com/diegomaneyro/Analytics/blob/main/imagenes/Analytics.jpeg"  height=300>
</p>


## **Impacto del COVID-19 en el mercado financiero y en la lista índice S&P500**
</br>

Es cierto que la pandemia del COVID-19 tuvo un impacto significativo en los mercados financieros en todo el mundo, incluyendo la lista índice S&P500. En particular, a principios de 2020, el mercado sufrió una gran caída en el precio de las acciones debido a la incertidumbre causada por la pandemia.

Si comparamos el comportamiento del índice S&P500 en los años previos al COVID-19 con el comportamiento durante la pandemia, podemos observar una diferencia significativa. Antes de la pandemia, el índice S&P500 mostraba una tendencia alcista estable, con fluctuaciones normales en el corto plazo. Sin embargo, a partir de marzo de 2020, el índice experimentó una fuerte caída, seguida de una recuperación rápida y volátil.

En consecuencia, una posible conclusión es que la pandemia del COVID-19 tuvo un impacto significativo en el mercado financiero y en la lista índice S&P500. El mercado experimentó una gran volatilidad y la recuperación ha sido inestable. Como resultado, es importante tener en cuenta los riesgos asociados con las inversiones financieras, ya que eventos imprevistos como una pandemia pueden tener un impacto significativo en el mercado y en las inversiones.


`EDA Y REPORTE`:
[link](https://github.com/diegomaneyro/Analytics/blob/main/EDA)

 Utilizando la libreria yfinance de python se ingesta el archivo csv con los datos del indice SP500, se filtro inicialmente los registros posteriores al año 2000.
 Luego de la exploracion de datos inicial, se visualiza con matplotlib y seaborn de python, para buscar correlación de variables, outliers y datos atipicos asi como patrones y tendencias.

`Analisis de riesgo`:
[link](https://github.com/diegomaneyro/Analytics/tree/main/An%C3%A1isis%20de%20Riesgo)

 Analisis sobre cuatro empresas elegidas del indice NASDAQ para observar los movimientos financieros, se desarrolla un Analisis de Riesgo para futura inversion: Apple, Microsoft, Amazon y Google.

`Analisis de crecimiento`:
[link](https://github.com/diegomaneyro/Analytics/blob/main/An%C3%A1lisis%20de%20Crecimiento/An%C3%A1lisis_crecimiento.ipynb)

 Análisis de crecimiento de cada empresa elejida para la recomendación de inversión

`Recomendación: Empresa y día`:
[link](https://github.com/diegomaneyro/Analytics/blob/main/An%C3%A1lisis%20de%20Crecimiento/readme.md)

 Se recomienda una empresa en base al análisis por empresa y la recomendación del día par la inversión

`Dashboard:`:
[link](https://github.com/diegomaneyro/Analytics/blob/main/reporte)

 Reporte de power bi de un historico del indice SP500 para los años posterior al 2000, y observacion de empresas especificas para posterior recomendacion de invesion, visualizando, precios de apertura, cierre, precios ajustados, desviacion estandar, filtrado por mes año y empresa

### Que día de la semana conviene invertir en bolsa::rocket::rocket::rocket::moneybag::moneybag:


:bangbang:
El **lunes** es historicamente el peor dia de la semana para invertir.Según un estudio de LPL Financial, el retorno medio del S&P 500 entre 1928 y 2017 durante los lunes es del -0,08%, el peor día de la semana con diferencia. Anualizando la rentabilidad que ofrecería invertir solo el primer día de la semana en el selectivo norteamericano se produciría una caída del 20%. Además, el 52% de los lunes acaban en rojo. 

:white_check_mark:
¿Qué sucede otros días?
Si el lunes históricamente la jornada menos indicada para buscar ganancias en bolsa, el mejor día para el inversor es el **miércoles**. De media, en la tercera sesión de la semana se sube un 0,08% y el 54% de los miércoles acaban en verde, siempre según el estudio de LPL Financial. Anualizando este comportamiento la subida sería del 20%.

:white_check_mark:
Mientras, el día en el que es más probable obtener retornos positivos es el **viernes**: el 54,5% de las veces la última sesión de la semana acaba con retornos positivos. La rentabilidad media obtenida ese día es del 0,05% y anualizar el dato histórico de los viernes implica un rendimiento del 13%.

Mientras, los martes se logran de media subidas del 0,05%, lo que anualizado implica una rentabilidad del 12,5%. El 51,7% de estos días se logran revalorizaciones en EEUU. Finalmente, el jueves es el segundo peor día de la semana, con un ascenso medio del 0,04%. El 52,5% de estos días acaba en positivo y su rendimiento anualizado supera el 10%

👉 Análisis de Crecimiento por empresa
Se aplicaron distintos KPIs:

📌 KPI Volatilidad

📌 KPI Margen bruto de beneficios

📌 KPI ingreso medio por usuario

📌 KPI tasa de crecimiento anual compuesta

Tambien se uso como indicador la desviación estándar de los precios de cierre de las acciones, para cada empresa en el periodo posterior al año 2000.

Recomendación de inversión: Teniendo en cuenta los resultados de los kpi, y los indicadores de la empresa, se recomienda la inversion en la empresa: Apple el día Miercoles


