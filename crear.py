# Cargar la clasificación de países por continente
df_continentes = pd.read_csv('paises.csv')  # Asegúrate de tener este archivo

# Unir los DataFrames
df_wine = df_wine.merge(df_continentes, left_on='pais', right_on='Country', how='left')

# Crear nuevas columnas
df_wine['continente'] = df_wine['Continent']  # Renombrar la columna
df_wine['precio_alto'] = df_wine['precio'] > 50  # Columna booleana
df_wine['calidad'] = df_wine['puntuacion'].apply(lambda x: 'Alta' if x >= 90 else 'Media' if x >= 80 else 'Baja')

print("\nNuevas columnas creadas:")
print(df_wine[['puntuacion', 'precio', 'continente', 'precio_alto', 'calidad']].head())
