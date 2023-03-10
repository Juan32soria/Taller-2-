# -*- coding: utf-8 -*-
"""IMDBAnalyticsColab_Workshop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/jdmartinev/IMDBAnalytics/blob/main/IMDBAnalyticsColab/IMDBAnalyticsColab_Workshop.ipynb

# Taller

Responder las preguntas de analítica acerca de la base de datos de IMDB que se encuentran a lo largo de este documento. Modifique el nombre de este archivo por el número de su documento (123456789.ipynb) y adjúntelo como parte de los entregables del taller.

Nombre:

### Descargar los datos:
- Tabla de películas
- Archivo .shp y archivos auxiliares con la información necesaria para pintar el mapa

Estos archivos quedarán en la carpeta _/content/IMDBAnalyticsData/_ asociada con el sistema operativo del servidor en el que se está ejecutando google colab.
"""

!wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1osH_xhTCW4Qh7f00VU_UaRK5whEXe8dr' -O data
!unzip "/content/data" -d "/content/IMDBAnalyticsData/"

"""
### Importar las librerías necesarias

La libreia geopandas, que sirve para el procesamiento de archivos con información geográfica (shapefiles) no está instalada por defecto en el ambiente de google colab. Por esta razón, debe instalarla"""

!pip install geopandas

import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

"""### Información básica de la tabla de películas"""

df = pd.read_csv('IMDBAnalyticsData/Data/movie_metadata.csv')
df.head()

"""**Pregunta 1**

Utilice histogramas para comparar la distribución de la columna _imdb_score_ relacionada con películas producidas en Francia y Canadá.

Para crear el histograma:

- Ajuste el número de _bins_ a 20
- De nombres a las etiquetas de los ejes (xAxis y yAxis)
- Remueva el _grid_
"""

df['imdb_score'] == "Francia" 
df['imdb_score'] == "Canada"

ax = df["imdb_score"].hist(bins = 20)
ax.set_xlabel('xAxis')
ax.set_ylabel('yAxis')

"""**Pregunta 2**

Cree un histograma para mirar la distribución de la columna _imdb_score_ de las películas producidas en blanco y negro.

Para crear el histograma:

- Ajuste el número de _bins_ a 10
- De nombres a las etiquetas de los ejes (xAxis y yAxis)
- Remueva el _grid_
"""

df_low_score = df[df['imdb_score'] == "Black and White" ]
df_low_score

"""**Pregunta 3**

¿Qué país tiene el mayor promedio de calificación de películas? Utilice figuras de barras para visualizar los resultados.  


"""

df_country = df.groupby('country').agg({'imdb_score': 'mean'}).reset_index()
fig = px.bar(df_country.head(10), x='country', y='imdb_score',
             title='Los 10 países con las calificaciones promedio más altas')
fig.show()

"""**Pregunta 4** 

¿Cuántas películas a blanco y negro y cuántas películas a color se tienen en la base de datos?

"""

color = df.groupby('color').size().to_frame('Black and withe')
color

"""**Pregunta 5**

¿Cuál película de Christopher Nolan tiene la mayor calificación (_imdb_score_)? Utilice figuras de barras para visualizar los resultados.
"""

name = df[df['director_name'] == 'Christopher Nolan']
calificacion = name['imdb_score'].idxmax()

print(f"La película con mayor calificacion de Christopher Nolan es: {df.iloc[calificacion]['movie_title']} con una calificación de: {name['imdb_score'].max()}")
fig = px.bar(x = name['movie_title'], y = name['imdb_score'], labels={'y':'Calificacion', 'x':'Paises'})
fig.show()

"""**Pregunta 6**

Utilice un _line chart_ para visualizar cuántas películas se produjeron en USA desde el 2010 hasta el 2015.
"""

df_usa = df[(df['country'] == 'USA') & (df['title_year'] >= 2010) & (df['title_year'] <= 2015)]
df_year = df_usa.groupby('title_year')['movie_title'].count()
plt.plot(df_year.index, df_year.values)
plt.xlabel('Año')
plt.ylabel('Número de películas')
plt.title('Producción de películas en EE. UU. (2010-2015)')
plt.show()

"""**Pregunta 7**

Grafique en un mapa el _imdb_score_ promedio de las películas producidas en cada país.
"""

df_grouped = df.groupby("country")["imdb_score"].mean().reset_index()
fig = px.choropleth(df_grouped, locations="country", locationmode="country names", color="imdb_score", 
                    hover_name="country", range_color=(0, 10), 
                    title="IMDB Score promedio de películas por país")
fig.update_layout(mapbox_style="open-street-map")
fig.show()

"""**Pregunta 8**

¿Qué información de su proyecto podría utilizar para hacer analítica de datos?

"""

