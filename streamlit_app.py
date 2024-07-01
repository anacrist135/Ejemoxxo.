!pip install streamlit pandas openpyxl
import streamlit as st
import pandas as pd

# Crear un DataFrame vacío con las columnas necesarias
df = pd.DataFrame(columns=['Número de Empleado', 'Trabajo Realizado', 'Tiempo Tardado (min)'])

# Función para añadir datos al DataFrame
def add_data(employee_id, work_done, time_spent):
    global df
    new_row = {'Número de Empleado': employee_id, 'Trabajo Realizado': work_done, 'Tiempo Tardado (min)': time_spent}
    df = df.append(new_row, ignore_index=True)

# Interfaz de Streamlit
st.title('Encuesta de Trabajo Realizado')

employee_id = st.text_input('Número de Empleado')
work_done = st.text_input('Trabajo Realizado')
time_spent = st.number_input('Tiempo Tardado (min)', min_value=0)

if st.button('Añadir Datos'):
    add_data(employee_id, work_done, time_spent)
    st.success('Datos añadidos exitosamente')

if st.button('Guardar en Excel'):
    df.to_excel('datos_empleados.xlsx', index=False)
    st.success('Datos guardados en "datos_empleados.xlsx"')

# Mostrar DataFrame
st.write(df)
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
