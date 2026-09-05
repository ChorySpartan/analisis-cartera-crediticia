import pandas as pd

clientes = pd.read_csv('datos/clientes_limpio.csv')
prestamos = pd.read_csv('datos/prestamos.csv')
pagos = pd.read_csv('datos/pagos.csv')

# Paso 1: préstamos + clientes

df1 = prestamos.merge(clientes, on='cliente_id', how='inner')
print(f"dfq (préstamos + clientes): {df1.shape}")

# Paso 2: df1 + pagos

df_completo = df1.merge(pagos, on='prestamo_id', how='inner')
print(f"df_completo (todo unido): {df_completo.shape}")

print(df_completo.columns.tolist())
print(df_completo.head())

# Paso 3 groupby()

mora_por_producto = df_completo.groupby('producto')['estado'].apply(
    lambda x: (x == 'Atrasado').mean() * 100
).round(1)

mora_general = (df_completo['estado'] == 'Atrasado').mean() * 100
print(f"Mora general de la cartera: {mora_general:.1f}%")

print(mora_por_producto)














































































































