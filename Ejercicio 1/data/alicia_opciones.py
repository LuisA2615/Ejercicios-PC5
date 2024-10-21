import pandas as pd

# Cargar los datos
df_airbnb = pd.read_csv("./data/airbnb.csv")

# Filtrar propiedades para Alicia
alicia_options = df_airbnb[
    (df_airbnb['reviews'] > 10) & 
    (df_airbnb['overall_satisfaction'] > 4)
]

# Ordenar por puntuación y luego por número de reseñas
alicia_options_sorted = alicia_options.sort_values(
    by=['overall_satisfaction', 'reviews'],
    ascending=[False, False]  # Primero por satisfacción (desc), luego por reseñas (desc)
)

# Obtener las 3 mejores alternativas
top_alternatives = alicia_options_sorted.head(3)

# Mostrar resultados
print("Opciones para Alicia:")
print(top_alternatives[['room_id', 'host_id', 'room_type', 'neighborhood', 'reviews', 'overall_satisfaction', 'accommodates', 'bedrooms', 'price']])
