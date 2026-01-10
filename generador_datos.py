import pandas as pd 
import numpy as np 
import random 
from datetime import datetime, timedelta

#Configuracion de los datos modelos
filas = 1000
productos = ["Tarjetas","Volantes","Lonas","Vinilos","Vinilo de corte","Libros"]
estados= ["Entregado","Entregado","Entregado","En proceso","cancelado"]
data = {
    "ID_Orden": range(1000,1000 + filas),
    "Fecha": [datetime(2024,1,1)+ timedelta(days=random.randint(0,365))for _ in range(filas)],
    "Producto": [random.choice(productos) for _ in range(filas)],
    "Cliente": [f"Cliente_{random.randint(1,50)}" for _ in range(filas)],
    "Estado":[random.choice(estados) for _ in range(filas)],
    "Costo_Produccion": np.random.uniform(5000,50000,filas).round(2)
}
df = pd.DataFrame(data)
df["Precio_Venta"] = (df["Costo_Produccion"] * np.random.uniform(1.3,1.8,filas)).round(2)
df["Margen"] = df["Precio_Venta"] - df["Costo_Produccion"]

df.to_csv("datos_imprenta.csv",index=False)
print("Archivo generado con exito.")