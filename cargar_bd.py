import pandas as pd
import sqlite3

clientes = pd.read_csv('datos/clientes_limpio.csv')
prestamos = pd.read_csv('datos/prestamos.csv')
pagos = pd.read_csv('datos/pagos.csv')

conexion = sqlite3.connect('cartera.db')

clientes.to_sql('clientes', conexion, if_exists='replace', index=False)
prestamos.to_sql('prestamos', conexion, if_exists='replace', index=False)
pagos.to_sql('pagos', conexion, if_exists='replace', index=False)

conexion.close()

print("Base de datos actualizada: clientes, prestamos, pagos")




































































































