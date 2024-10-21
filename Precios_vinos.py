# Vinos con precio alto y buena puntuación
report4 = df_wine[(df_wine['precio_alto'] == True) & (df_wine['puntuacion'] >= 85)]
print("\nVinos con precio alto y buena puntuación:")
print(report4[['pais', 'variedad', 'precio', 'puntuacion']].head())
