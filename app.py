import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación (Requisito: Al menos un encabezado)
st.header('Anuncios de Venta de Coches Usados')

# Cargar el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

st.write("Selecciona una opción para generar un gráfico:")

# Casilla de verificación para el Histograma (Requisito: Histograma y Botón/Checkbox)
build_histogram = st.checkbox('Mostrar Histograma de Odómetro')

if build_histogram:
    st.write('Creando un histograma para la distribución del millaje (odómetro)...')

    # Crear un histograma
    fig_hist = px.histogram(
        car_data, x="odometer", color="condition", title="Distribución del Odómetro")

    st.plotly_chart(fig_hist, use_container_width=True)


# Casilla de verificación para el Gráfico de Dispersión (Requisito: Gráfico de Dispersión y Botón/Checkbox)
build_scatter = st.checkbox(
    'Mostrar Gráfico de Dispersión (Precio vs. Odómetro)')

if build_scatter:
    st.write('Creando un gráfico de dispersión para precio vs. odómetro...')

    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data,
                             x="odometer",
                             y="price",
                             color="type",
                             title="Precio vs. Odómetro por Tipo de Vehículo")

    st.plotly_chart(fig_scatter, use_container_width=True)
