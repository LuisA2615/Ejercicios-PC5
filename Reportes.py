# Reporte por continente
report1 = df_wine.groupby('continente')['puntuacion'].max().reset_index()
print("\nVinos mejor puntuados por continente:")
print(report1)
