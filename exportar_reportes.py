# Exportar reportes a diferentes formatos
report1.to_csv('mejores_vinos_por_continente.csv', index=False)
report2.to_excel('promedio_precio_y_reseñas.xlsx', index=False)
report3.to_sql('vinos_por_variedad', con='sqlite:///vinos.db', index=False)
report4.to_json('vinos_precios_altos.json', orient='records')

print("Reportes exportados a diferentes formatos.")
