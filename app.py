import streamlit as st
import pandas as pd
import plotly.express as px

try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encuentra.")
    st.stop()  # Se detiene la aplicación

# --- Contenido de la aplicación ---

# 1. Encabezado: Se necesita al menos un encabezado
st.header("Análisis de anuncios de venta de vehiculos usados")
st.markdown("---")

st.write(
    """
    Esta aplicación te permite explorar visualmente el conjunto de datos de anuncios de venta de coches.
    Utiliza las casillas de verificación a continuación para generar gráficos interactivos.
    """
)

# 2. Controles interactivos para la casilla de verficiación
build_histogram = st.checkbox('Construir Histograma de Millaje (Odómetro)')

if build_histogram:
    # Escribir mensaje
    st.write('Distribución de Millaje por Condición del Vehículo:')

    # Crear un histograma (Requisito: Al menos un histograma)
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        color="condition",
        title="Histograma de Odómetro"
    )

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)


# Casilla de verificación para el Gráfico de Dispersión
build_scatter = st.checkbox(
    'Construir Gráfico de Dispersión (Precio vs. Millas recorridas)')

if build_scatter:
    # Escribir mensaje
    st.write('Relación entre el Precio y las millas de los Vehículos:')

    # Crear un gráfico de dispersión (Requisito: Al menos un gráfico de dispersión)
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="type",
        title="Precio vs. Odómetro por Tipo de Vehículo"
    )

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
