import pandas as pd
import numpy as np

# Cargar los datos originales
clientes = pd.read_csv('datos/clientes.csv')
prestamos = pd.read_csv('datos/prestamos.csv')
pagos = pd.read_csv('datos/pagos.csv')

def ensuciar_datos(df, columna_texto, columna_numerica):
    df_sucio = df.copy()

    # Insertar algunos valores nulos al azar
    filas_nulas = df_sucio.sample(frac=0.03).index
    df_sucio.loc[filas_nulas, columna_numerica] = np.nan

    # Duplicar algunas filas
    duplicados = df_sucio.sample(frac=0.02)
    df_sucio = pd.concat([df_sucio, duplicados], ignore_index=True)

    return df_sucio

clientes_sucio = ensuciar_datos(clientes, 'nombre', 'ingreso_mensual')
clientes_sucio.to_csv('datos/clientes_sucio.csv', index=False, encoding='utf-8-sig')

print(f"Clientes original: {len(clientes)} filas")
print(f"Clientes sucio: {len(clientes_sucio)} filas")
print(f"Nulos en ingreso_mensual: {clientes_sucio['ingreso_mensual'].isna().sum()}")











































































































