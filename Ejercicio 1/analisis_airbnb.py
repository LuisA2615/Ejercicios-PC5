import pandas as pd

# Cargar los datos
df_airbnb = pd.read_csv("./data/airbnb.csv")

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df_airbnb.head())

# Mostrar información general sobre el DataFrame
print("\nInformación del DataFrame:")
print(df_airbnb.info())

# Mostrar la forma del DataFrame (filas, columnas)
print("\nForma del DataFrame:")
print(df_airbnb.shape)

# Mostrar los nombres de las columnas
print("\nNombres de las columnas:")
print(df_airbnb.columns)

# Estadísticas descriptivas del DataFrame
print("\nEstadísticas descriptivas:")
print(df_airbnb.describe())

# Verificar si hay valores nulos en el DataFrame
print("\nValores nulos en el DataFrame:")
print(df_airbnb.isnull().sum())

# Verificar los tipos de datos de las columnas
print("\nTipos de datos de las columnas:")
print(df_airbnb.dtypes)

# Contar el número de propiedades por tipo
print("\nNúmero de propiedades por tipo:")
print(df_airbnb['room_type'].value_counts())

# Contar el número de propiedades por barrio
print("\nNúmero de propiedades por barrio:")
print(df_airbnb['neighborhood'].value_counts())

# Histograma de precios
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(df_airbnb['price'], bins=30, color='blue', edgecolor='black')
plt.title('Distribución de Precios de Airbnb en Lisboa')
plt.xlabel('Precio (euros)')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.show()
