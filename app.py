import streamlit as st
import pandas as pd
import plotly.express as px

try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encuentra.")
    st.stop()  # Se detiene la aplicación

# --- Contenido de la aplicación ---
