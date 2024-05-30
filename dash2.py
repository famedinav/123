import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Supongamos que estos son tus dataframes de predicciones ya preparados
# forecast_df y forecast_df_min

# Aquí incluimos los dataframes de ejemplo
forecast_dates = pd.date_range(start='2024-04-13', periods=7)

# Ejemplo de datos de predicción de llamadas
forecast_df = pd.DataFrame({
    'FECHA': forecast_dates,
    'FORECAST_LLAMADAS_ICT': [12192510, 13439290, 14691170, 15280160, 15055220, 15735120, 14198120],
    'FORECAST_LLAMADAS_AA': [11434580, 11810330, 12173000, 12268240, 12099050, 12407660, 12167830],
    'FORECAST_LLAMADAS_TOL_DWT': [1575128, 1702692, 1820361, 1875174, 1869402, 1946510, 1796517]
})

# Ejemplo de datos de predicción de minutos
forecast_df_min = pd.DataFrame({
    'FECHA': forecast_dates,
    'FORECAST_MINUTOS_ICT': [45043088, 45414449, 44678873, 44044524, 35755931, 40123567, 41234567],
    'FORECAST_MINUTOS_AA': [50151251, 50383967, 49567849, 49373343, 41120782, 42123456, 43234567],
    'FORECAST_MINUTOS_TOL_DWT': [20760467, 14157333, 14190862, 13911920, 9949498, 10123456, 11123456]
})

# Configurar la página de Streamlit
st.title('Dashboard de Predicciones de Llamadas y Minutos')
st.write('### Predicciones para los próximos 7 días')

# Mostrar los dataframes
st.write('#### Predicciones de Llamadas')
st.dataframe(forecast_df)

st.write('#### Predicciones de Minutos')
st.dataframe(forecast_df_min)

# Graficar los valores históricos y las predicciones
st.write('### Gráficas de Predicciones')

fig, axs = plt.subplots(3, 2, figsize=(14, 14))

# Aquí usaré valores ficticios para los históricos, debes reemplazarlos con tus datos reales
historical_ict_series = [10000000, 11000000, 11500000, 12000000, 12500000, 13000000, 13500000]
historical_aa_series = [9000000, 9500000, 9800000, 10000000, 10200000, 10500000, 10700000]
historical_tol_series = [5000000, 5200000, 5300000, 5400000, 5500000, 5600000, 5700000]

historical_ict_series_min = [30000000, 32000000, 34000000, 36000000, 38000000, 40000000, 42000000]
historical_aa_series_min = [25000000, 27000000, 29000000, 31000000, 33000000, 35000000, 37000000]
historical_tol_series_min = [15000000, 16000000, 17000000, 18000000, 19000000, 20000000, 21000000]

axs[0, 0].plot(forecast_df['FECHA'], historical_ict_series, label='Histórico')
axs[0, 0].plot(forecast_df['FECHA'], forecast_df['FORECAST_LLAMADAS_ICT'], label='Predicción')
axs[0, 0].set_title('Llamadas ICT')
axs[0, 0].legend()

axs[1, 0].plot(forecast_df['FECHA'], historical_aa_series, label='Histórico')
axs[1, 0].plot(forecast_df['FECHA'], forecast_df['FORECAST_LLAMADAS_AA'], label='Predicción')
axs[1, 0].set_title('Llamadas AA')
axs[1, 0].legend()

axs[2, 0].plot(forecast_df['FECHA'], historical_tol_series, label='Histórico')
axs[2, 0].plot(forecast_df['FECHA'], forecast_df['FORECAST_LLAMADAS_TOL_DWT'], label='Predicción')
axs[2, 0].set_title('Llamadas TOL')
axs[2, 0].legend()

axs[0, 1].plot(forecast_df_min['FECHA'], historical_ict_series_min, label='Histórico')
axs[0, 1].plot(forecast_df_min['FECHA'], forecast_df_min['FORECAST_MINUTOS_ICT'], label='Predicción')
axs[0, 1].set_title('Minutos ICT')
axs[0, 1].legend()

axs[1, 1].plot(forecast_df_min['FECHA'], historical_aa_series_min, label='Histórico')
axs[1, 1].plot(forecast_df_min['FECHA'], forecast_df_min['FORECAST_MINUTOS_AA'], label='Predicción')
axs[1, 1].set_title('Minutos AA')
axs[1, 1].legend()

axs[2, 1].plot(forecast_df_min['FECHA'], historical_tol_series_min, label='Histórico')
axs[2, 1].plot(forecast_df_min['FECHA'], forecast_df_min['FORECAST_MINUTOS_TOL_DWT'], label='Predicción')
axs[2, 1].set_title('Minutos TOL')
axs[2, 1].legend()

plt.tight_layout()
st.pyplot(fig)
