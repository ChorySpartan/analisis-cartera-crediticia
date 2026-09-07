import pandas as pd

clientes = pd.read_csv('datos/clientes_limpio.csv')
prestamos = pd.read_csv('datos/prestamos.csv')
pagos = pd.read_csv('datos/pagos.csv')

df1 = prestamos.merge(clientes, on='cliente_id', how='inner')
df_completo = df1.merge(pagos, on='prestamo_id', how='inner')

tabla_mora = df_completo.pivot_table(
    index='producto',
    columns='ocupacion',
    values='estado',
    aggfunc=lambda x: (x == 'Atrasado').mean() * 100
).round(1)

print(tabla_mora)




































































































