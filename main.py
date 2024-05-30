import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Cargar el conjunto de datos
file_path_llamadas = 'df_llamadas_model.csv'  # Cambia esto a la ruta correcta de tu archivo
df_llamadas = pd.read_csv(file_path_llamadas)

file_path_minutos = 'df_minutos_model.csv'  # Cambia esto a la ruta correcta de tu archivo
df_minutos = pd.read_csv(file_path_minutos)

# Convertir la columna 'FECHA' al formato datetime
df_llamadas['FECHA'] = pd.to_datetime(df_llamadas['FECHA'])
df_minutos['FECHA'] = pd.to_datetime(df_minutos['FECHA'])

# Establecer la columna 'FECHA' como índice
df_llamadas.set_index('FECHA', inplace=True)
df_minutos.set_index('FECHA', inplace=True)

# Preparar los datos para cada serie
ict_series = df_llamadas['TOTAL_LLAMADAS_ICT']
aa_series = df_llamadas['TOTAL_LLAMADAS_AA']
tol_series = df_llamadas['TOTAL_LLAMADAS_TOL_DWT']

ict_series_min = df_minutos['TOTAL_MINUTOS_ICT']
aa_series_min = df_minutos['TOTAL_MINUTOS_AA']
tol_series_min = df_minutos['TOTAL_MINUTOS_TOL_DWT']

# Dividir los datos en conjuntos de entrenamiento y prueba
train_ict = ict_series[:-7]
train_aa = aa_series[:-7]
train_tol = tol_series[:-7]

train_ict_min = ict_series_min[:-7]
train_aa_min = aa_series_min[:-7]
train_tol_min = tol_series_min[:-7]

# Ajustar el modelo ARIMA para cada serie
model_ict = ARIMA(train_ict, order=(5,1,0)).fit()
model_aa = ARIMA(train_aa, order=(5,1,0)).fit()
model_tol = ARIMA(train_tol, order=(5,1,0)).fit()

model_ict_min = ARIMA(train_ict_min, order=(5,1,0)).fit()
model_aa_min = ARIMA(train_aa_min, order=(5,1,0)).fit()
model_tol_min = ARIMA(train_tol_min, order=(5,1,0)).fit()

# Predecir los próximos 7 días
forecast_ict = model_ict.forecast(steps=7).round(0).astype(int)
forecast_aa = model_aa.forecast(steps=7).round(0).astype(int)
forecast_tol = model_tol.forecast(steps=7).round(0).astype(int)

forecast_ict_min = model_ict_min.forecast(steps=7).round(0).astype(int)
forecast_aa_min = model_aa_min.forecast(steps=7).round(0).astype(int)
forecast_tol_min = model_tol_min.forecast(steps=7).round(0).astype(int)

# Preparar un dataframe para mostrar los resultados de las predicciones
forecast_dates = pd.date_range(start=df_llamadas.index[-1] + pd.Timedelta(days=1), periods=7)
forecast_df = pd.DataFrame({
    'FECHA': forecast_dates,
    'FORECAST_LLAMADAS_ICT': forecast_ict,
    'FORECAST_LLAMADAS_AA': forecast_aa,
    'FORECAST_LLAMADAS_TOL_DWT': forecast_tol
})

forecast_df_min = pd.DataFrame({
    'FECHA': forecast_dates,
    'FORECAST_MINUTOS_ICT': forecast_ict_min,
    'FORECAST_MINUTOS_AA': forecast_aa_min,
    'FORECAST_MINUTOS_TOL_DWT': forecast_tol_min
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

axs[0, 0].plot(ict_series, label='Histórico')
axs[0, 0].plot(forecast_dates, forecast_ict, label='Predicción')
axs[0, 0].set_title('Llamadas ICT')
axs[0, 0].legend()

axs[1, 0].plot(aa_series, label='Histórico')
axs[1, 0].plot(forecast_dates, forecast_aa, label='Predicción')
axs[1, 0].set_title('Llamadas AA')
axs[1, 0].legend()

axs[2, 0].plot(tol_series, label='Histórico')
axs[2, 0].plot(forecast_dates, forecast_tol, label='Predicción')
axs[2, 0].set_title('Llamadas TOL')
axs[2, 0].legend()

axs[0, 1].plot(ict_series_min, label='Histórico')
axs[0, 1].plot(forecast_dates, forecast_ict_min, label='Predicción')
axs[0, 1].set_title('Minutos ICT')
axs[0, 1].legend()

axs[1, 1].plot(aa_series_min, label='Histórico')
axs[1, 1].plot(forecast_dates, forecast_aa_min, label='Predicción')
axs[1, 1].set_title('Minutos AA')
axs[1, 1].legend()

axs[2, 1].plot(tol_series_min, label='Histórico')
axs[2, 1].plot(forecast_dates, forecast_tol_min, label='Predicción')
axs[2, 1].set_title('Minutos TOL')
axs[2, 1].legend()

plt.tight_layout()
st.pyplot(fig)
