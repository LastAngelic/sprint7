import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Encabezado de la aplicación
st.header("Análisis de anuncios de venta de coches")

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')

    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs odómetro')

    fig = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(opacity=0.5)
    )])

    fig.update_layout(title_text='Precio vs Odómetro')

    st.plotly_chart(fig, use_container_width=True)
