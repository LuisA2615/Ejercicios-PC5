import pandas as pd

# Cargar los datos
df_airbnb = pd.read_csv("./data/airbnb.csv")

# Filtrar propiedades de Roberto y Clara
roberto_id = 97503
clara_id = 90387

# Filtrar las propiedades
roberto_property = df_airbnb[df_airbnb['room_id'] == roberto_id]
clara_property = df_airbnb[df_airbnb['room_id'] == clara_id]

# Combinar en un nuevo DataFrame
df_roberto_clara = pd.concat([roberto_property, clara_property])

# Guardar el DataFrame en un archivo Excel
df_roberto_clara.to_excel("roberto.xls", index=False)

print("Archivo 'roberto.xls' guardado con las propiedades de Roberto y Clara.")
