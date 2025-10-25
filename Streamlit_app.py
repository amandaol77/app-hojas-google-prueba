import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(layout="centered", page_title="App de Prueba GSheets - Dos Hojas")
st.title("✅ ¡Conexión GSheets de Prueba para Dos Hojas!")
st.markdown("Si ves el contenido de ambas hojas, ¡la conexión de Secrets funciona!")

# ----------------------------------------------------
# CONFIGURACIÓN DE LAS URLS (Ya insertadas y verificadas)
# ----------------------------------------------------
URL_HOJA_1 = "https://docs.google.com/spreadsheets/d/1G6V65-y81QryxPV6qKZBX4ClccTrVYbAAB7FBT9tuKk/edit?usp=drivesdk" 
URL_HOJA_2 = "https://docs.google.com/spreadsheets/d/1XwYeFGGBF9M2CuY3-8nBUnyzkqsR1U_xEpHxrmHOqR4/edit?usp=drivesdk" 
# ----------------------------------------------------


try:
    # 1. Crear conexión (usa automáticamente 'gserviceaccount' de st.secrets)
    conn = st.connection("gsheets", type=GSheetsConnection)

    
    st.header("Hoja de Cálculo #1: INVENTARIO")
    # 2. Leer datos de la HOJA 1
    data_hoja_1 = conn.read(spreadsheet=URL_HOJA_1, ttl=5)

    # 3. Mostrar datos de la HOJA 1
    st.subheader("Datos de Inventario")
    st.dataframe(data_hoja_1)


    st.header("Hoja de Cálculo #2: VENTAS")
    # 2. Leer datos de la HOJA 2
    data_hoja_2 = conn.read(spreadsheet=URL_HOJA_2, ttl=5)
    
    # 3. Mostrar datos de la HOJA 2
    st.subheader("Datos de Ventas")
    st.dataframe(data_hoja_2)


except Exception as e:
    st.error(f"Error de conexión. Detalles: {e}")
    st.info("El problema ahora es de PERMISOS o APIs. Asegúrate de que el Service Account tenga permiso de Editor en ambas hojas.")
