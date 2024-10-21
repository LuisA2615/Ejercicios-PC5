# Conteo de vinos por variedad
report3 = df_wine['variedad'].value_counts().reset_index()
report3.columns = ['variedad', 'conteo']
print("\nConteo de vinos por variedad:")
print(report3.head())
