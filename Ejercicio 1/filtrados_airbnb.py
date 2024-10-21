import pandas as pd

# Cargar los datos
df_airbnb = pd.read_csv("./data/airbnb.csv")

# Filtrar propiedades que tienen una puntuación media (overall_satisfaction) mayor a 4
altas_satisfacciones = df_airbnb[df_airbnb['overall_satisfaction'] > 4]
print("\nPropiedades con satisfacción general mayor a 4:")
print(altas_satisfacciones.head())

# Filtrar propiedades que pueden acomodar más de 4 personas
accommodates_mas_4 = df_airbnb[df_airbnb['accommodates'] > 4]
print("\nPropiedades que acomodan más de 4 personas:")
print(accommodates_mas_4.head())

# Filtrar propiedades en un barrio específico (por ejemplo, 'Alfama')
alfama_properties = df_airbnb[df_airbnb['neighborhood'] == 'Alfama']
print("\nPropiedades en el barrio 'Alfama':")
print(alfama_properties.head())

# Filtrar propiedades de tipo 'Entire home/apt' y que tienen un precio menor a 100 euros
economicas = df_airbnb[(df_airbnb['room_type'] == 'Entire home/apt') & (df_airbnb['price'] < 100)]
print("\nPropiedades económicas (entire home/apt) por debajo de 100 euros:")
print(economicas.head())

# Filtrar las 5 propiedades más caras
top_caras = df_airbnb.sort_values(by='price', ascending=False).head(5)
print("\nLas 5 propiedades más caras:")
print(top_caras)

# Filtrar las 5 propiedades con más reseñas
top_reseñas = df_airbnb.sort_values(by='reviews', ascending=False).head(5)
print("\nLas 5 propiedades con más reseñas:")
print(top_reseñas)
