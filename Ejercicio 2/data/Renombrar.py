# Renombrar columnas
df_wine.rename(columns={
    'points': 'puntuacion',
    'price': 'precio',
    'country': 'pais',
    'variety': 'variedad'
}, inplace=True)

print("\nNuevos nombres de columnas:")
print(df_wine.columns)
