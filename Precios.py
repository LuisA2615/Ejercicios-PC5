# Promedio de precio y cantidad de reseñas según país
report2 = df_wine.groupby('pais').agg({'precio': 'mean', 'reviews': 'count'}).reset_index()
report2 = report2.sort_values(by='precio', ascending=False)
print("\nPromedio de precio y cantidad de reseñas según país:")
print(report2)
