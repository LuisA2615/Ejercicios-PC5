import pandas as pd

# Cargar los datos
df_airbnb = pd.read_csv("./data/airbnb.csv")

# Filtrar propiedades dentro del presupuesto
diana_options = df_airbnb[df_airbnb['price'] <= 50]

# Filtrar habitaciones compartidas y ordenar por puntuación
shared_rooms = diana_options[diana_options['room_type'] == 'Shared room']
shared_rooms_sorted = shared_rooms.sort_values(by='overall_satisfaction', ascending=False)

# Obtener las 10 propiedades más baratas (dentro de las compartidas)
top_shared_rooms = shared_rooms_sorted.head(10)

# Mostrar resultados
print("Opciones para Diana:")
print(top_shared_rooms[['room_id', 'host_id', 'room_type', 'neighborhood', 'reviews', 'overall_satisfaction', 'accommodates', 'bedrooms', 'price']])
