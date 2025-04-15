
import streamlit as st
import pandas as pd

# Cargar datos
df = pd.read_csv("datos.csv", parse_dates=["fecha"])

# Título
st.title("Filtrado interactivo de productos")

# Widgets de filtro
producto = st.text_input("Buscar producto:")
fecha = st.date_input("Desde fecha:")

# Filtro
df_filtrado = df.copy()
if producto:
    df_filtrado = df_filtrado[df_filtrado["producto"].str.contains(producto, case=False)]

if fecha:
    df_filtrado = df_filtrado[df_filtrado["fecha"] >= pd.to_datetime(fecha)]

# Mostrar resultado
st.subheader("Datos filtrados")
st.dataframe(df_filtrado)

# Descargar Excel
st.download_button(
    "Descargar Excel",
    df_filtrado.to_excel(index=False),
    file_name="resultado_filtrado.xlsx"
)
