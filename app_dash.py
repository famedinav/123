import streamlit as st
from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Conexión a MongoDB Atlas
@st.cache_resource
def init_connection():
    uri = "MONGODB_URI=mongodb+srv://jmorenoh4:H80i147g*28-@cluster0.ybqahf8.mongodb.net/"  # Reemplaza esto con tu URI de conexión de MongoDB Atlas
    client = MongoClient(uri)
    return client

client = init_connection()
db = client["interconexion"]  # Reemplaza con el nombre de tu base de datos
collection = db["df_grouped_tol_minutos"]  # Reemplaza con el nombre de tu colección


# Obtener datos de MongoDB
@st.cache_data(ttl=600)
def get_data():
    data = list(collection.find())
    return data

data = get_data()

# Convertir datos a DataFrame de Pandas
df = pd.DataFrame(data)

# Visualización con Streamlit
st.title("Dashboard con Streamlit y MongoDB Atlas")

st.write("### Datos de la base de datos")
st.write(df)

# Ejemplo de gráfico
if not df.empty:
    st.write("### Gráfico de ejemplo")
    st.bar_chart(df["campo_de_interés"])  # Reemplaza "campo_de_interés" por un campo numérico de tu colección
