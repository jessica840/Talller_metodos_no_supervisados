

import pandas as pd
import random
from datetime import timedelta, datetime

# Generar fechas de salida y llegada
def generar_hora_inicio():
    # Definir una hora de inicio base (por ejemplo, 6:00 AM)
    hora_inicio = datetime.strptime('06:00', '%H:%M')
    # Generar una hora de salida aleatoria
    return hora_inicio + timedelta(minutes=random.randint(0, 600))  # Aleatorio entre 0 y 600 minutos

# Crear un dataset sintético
data = []

# Generar 50 filas de datos
for i in range(50):
    id_ruta = i + 1
    origen = random.choice(['Estación A', 'Estación B', 'Estación C'])
    destino = random.choice(['Estación A', 'Estación B', 'Estación C'])
    while destino == origen:
        destino = random.choice(['Estación A', 'Estación B', 'Estación C'])
    hora_salida = generar_hora_inicio()
    hora_llegada = hora_salida + timedelta(minutes=random.randint(20, 60))  # Tiempo de viaje entre 20 y 60 minutos
    pasajeros = random.randint(10, 100)  # Número aleatorio de pasajeros entre 10 y 100
    tiempo_espera = random.randint(5, 20)  # Tiempo de espera aleatorio entre 5 y 20 minutos
    
    # Agregar los datos a la lista
    data.append([id_ruta, origen, destino, hora_salida.strftime('%H:%M'), hora_llegada.strftime('%H:%M'), pasajeros, tiempo_espera])

# Crear el DataFrame con los datos generados
df = pd.DataFrame(data, columns=['ID_Ruta', 'Origen', 'Destino', 'Hora_Salida', 'Hora_Llegada', 'Pasajeros', 'Tiempo_Espera'])

# Mostrar las primeras filas del dataset generado
print(df.head())

# Guardar el dataset en un archivo CSV si lo deseas
df.to_csv('dataset_transporte_masivo.csv', index=False)
