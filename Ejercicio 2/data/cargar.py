import pandas as pd

# Cargar el archivo CSV
df_wine = pd.read_csv('winemag-data-130k-v2.csv')

# Explorar el DataFrame
print("Primeras filas del DataFrame:")
print(df_wine.head())

print("\nInformación del DataFrame:")
print(df_wine.info())

print("\nEstadísticas descriptivas:")
print(df_wine.describe())
