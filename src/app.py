import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# Configuración de la Página
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Análisis de Airbnb en Madrid", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# Función de Carga y Limpieza de Datos (con Caché)
# -----------------------------------------------------------------------------
@st.cache_data
def load_and_clean_data(file_path):
    """
    Carga y limpia los datos de Airbnb desde una ruta de archivo especificada.
    """
    df = pd.read_csv(file_path, compression='gzip')
    
    columns_to_keep = [
        'id', 'name', 'host_id', 'host_is_superhost', 'neighbourhood_cleansed', 
        'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 
        'bathrooms_text', 'bedrooms', 'beds', 'price', 'number_of_reviews', 
        'review_scores_rating'
    ]
    df_clean = df[columns_to_keep].copy()

    df_clean['price'] = df_clean['price'].str.replace('[$,]', '', regex=True).astype(float)
    df_clean['host_is_superhost'].fillna('f', inplace=True)
    df_clean.dropna(inplace=True)

    return df_clean

# -----------------------------------------------------------------------------
# Carga Inicial de Datos
# -----------------------------------------------------------------------------
try:
    df = load_and_clean_data('data/listings.csv.gz')
except FileNotFoundError:
    st.error("Error: No se encontró el archivo de datos 'listings.csv.gz'. Asegúrate de que está en la carpeta 'data' en la raíz del proyecto.")
    st.stop()

# -----------------------------------------------------------------------------
# Título y Descripción de la Aplicación
# -----------------------------------------------------------------------------
st.title('🏘️ Dashboard Interactivo de Airbnb en Madrid')
st.markdown("""
Bienvenido a este dashboard interactivo para el análisis de datos de Airbnb en Madrid.
Utiliza los filtros en la barra lateral izquierda para explorar las propiedades según tus preferencias.
""")

# -----------------------------------------------------------------------------
# Barra Lateral (Sidebar) con Filtros Interactivos
# -----------------------------------------------------------------------------
st.sidebar.header('Filtros de Búsqueda')

# --- Filtro por barrio (CORREGIDO) ---
neighbourhoods = sorted(df['neighbourhood_cleansed'].unique())
desired_default_neighbourhoods = ['Centro', 'Salamanca', 'Chamberí']
actual_defaults = [n for n in desired_default_neighbourhoods if n in neighbourhoods]
if not actual_defaults and neighbourhoods:
    actual_defaults = neighbourhoods[:3]

selected_neighbourhoods = st.sidebar.multiselect(
    'Selecciona el/los barrio(s):',
    options=neighbourhoods,
    default=actual_defaults
)

# Filtro por tipo de habitación
room_types = sorted(df['room_type'].unique())
selected_room_types = st.sidebar.multiselect(
    'Selecciona el tipo de habitación:',
    options=room_types,
    default=room_types
)

# Filtro por rango de precios
price_min = int(df['price'].min())
price_max = int(df['price'].quantile(0.99))
selected_price = st.sidebar.slider(
    'Rango de precios (€):',
    min_value=price_min,
    max_value=price_max,
    value=(price_min, price_max)
)

# -----------------------------------------------------------------------------
# Lógica de Filtrado del DataFrame
# -----------------------------------------------------------------------------
if not selected_neighbourhoods or not selected_room_types:
    df_filtered = pd.DataFrame()
else:
    df_filtered = df[
        (df['neighbourhood_cleansed'].isin(selected_neighbourhoods)) &
        (df['room_type'].isin(selected_room_types)) &
        (df['price'] >= selected_price[0]) &
        (df['price'] <= selected_price[1])
    ]

# -----------------------------------------------------------------------------
# Cuerpo Principal de la Aplicación
# -----------------------------------------------------------------------------
st.header(f'Resultados de la Búsqueda')

total_listings = len(df_filtered)
avg_price = df_filtered['price'].mean() if total_listings > 0 else 0

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Alojamientos Encontrados", value=f"{total_listings:,}")
with col2:
    st.metric(label="Precio Promedio por Noche", value=f"{avg_price:.2f} €")

st.header('Ubicación de los Alojamientos')
if not df_filtered.empty:
    st.map(df_filtered[['latitude', 'longitude']])
else:
    st.warning("No se encontraron alojamientos con los filtros seleccionados. Por favor, amplía tus criterios de búsqueda.")

st.header('Datos Detallados')
if not df_filtered.empty:
    st.dataframe(
        df_filtered[[
            'name', 'neighbourhood_cleansed', 'room_type', 'price', 
            'review_scores_rating', 'accommodates'
        ]].head(100),
        height=300
    )
else:
    st.info("La tabla de datos aparecerá aquí una vez que se encuentren resultados.")