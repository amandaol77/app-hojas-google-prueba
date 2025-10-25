import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(layout="centered", page_title="App de Prueba GSheets - Dos Hojas")
st.title("✅ ¡Conexión GSheets de Prueba para Dos Hojas!")
st.markdown("Si ves el contenido de ambas hojas, ¡la conexión de Secrets funciona!")

# ----------------------------------------------------
# CONFIGURACIÓN: REEMPLAZA ESTAS URLs
# ----------------------------------------------------
URL_HOJA_1 = "https://docs.google.com/spreadsheets/d/1G6V65-y81QryxPV6qKZBX4ClccTrVYbAAB7FBT9tuKk/edit?usp=drivesdk" 
URL_HOJA_2 = "https://docs.google.com/spreadsheets/d/1XwYeFGGBF9M2CuY3-8nBUnyzkqsR1U_xEpHxrmHOqR4/edit?usp=drivesdk" 
# ----------------------------------------------------


try:
    # 1. Crear conexión
    # El objeto 'conn' usa automáticamente la clave 'gserviceaccount' de st.secrets
    conn = st.connection("gsheets", type=GSheetsConnection)

    
    st.header("Hoja de Cálculo #1")
    # 2. Leer datos de la HOJA 1
    data_hoja_1 = conn.read(spreadsheet=URL_HOJA_1, ttl=5)

    # 3. Mostrar datos de la HOJA 1
    st.subheader("Datos de Hoja 1")
    st.dataframe(data_hoja_1)


    st.header("Hoja de Cálculo #2")
    # 2. Leer datos de la HOJA 2
    data_hoja_2 = conn.read(spreadsheet=URL_HOJA_2, ttl=5)
    
    # 3. Mostrar datos de la HOJA 2
    st.subheader("Datos de Hoja 2")
    st.dataframe(data_hoja_2)

    # Opcional: Combinar las hojas en un solo DataFrame de Pandas (si tu lógica lo requiere)
    # datos_combinados = pd.concat([data_hoja_1, data_hoja_2])


except Exception as e:
    st.error("Error Crítico de Conexión. Revisa la consola de Streamlit para más detalles.")
    st.info("Asegúrate de:")
    st.markdown("- La clave 'gserviceaccount' esté **correctamente pegada** en Secrets (el formato de triple comilla).")
    st.markdown(f"- **Ambas URLs** en el código sean correctas.")
    st.markdown(f"- Tu Service Account (app-martin-clave-nueva-final@...) tenga permiso de **Editor** en ambas hojas.")
