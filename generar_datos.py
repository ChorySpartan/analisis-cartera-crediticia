from faker import Faker
import csv
import random

#Clientes

fake = Faker('es_ES')
Faker.seed(42)
random.seed(42)

def generar_clientes(cantidad=500):
    clientes = []
    for i in range(1, cantidad + 1):
        cliente = {
            'cliente_id': i,
            'nombre': fake.name(),
            'edad': random.randint(21, 70),
            'ingreso_mensual': round(random.uniform(2500, 25000), 1),
            'ocupacion': random.choice(['Empleado', 'Independiente', 'Empresario']),
            'Fecha_registro': fake.date_between(start_date='-5y', end_date='today'),
        }
        clientes.append(cliente)
    return clientes

def guardar_csv(datos, nombre_archivo):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=datos[0].keys())
        writer.writeheader()
        writer.writerows(datos)

#Prestámos

def generar_prestamos(clientes):
    prestamos = []
    prestamo_id = 1
    for cliente in clientes:
        num_prestamos = random.randint(1, 3)
        for _ in range(num_prestamos):
            prestamo = {
                'prestamo_id': prestamo_id,
                'cliente_id': cliente['cliente_id'],
                'monto': round(random.uniform(1000, 100000), 2),
                'tasa_intereses': round(random.uniform(8, 24), 2),
                'plazo_meses': random.choice([6, 12, 24, 36, 48, 60]),
                'producto': random.choice(['Personal', 'Hipotecario', 'Vehicular', 'Tarjeta de Crédito']),
                'fecha_originacion': fake.date_between(start_date='-4y', end_date='today'),
            }
            prestamos.append(prestamo)
            prestamo_id += 1
    return prestamos

#Pagos

def generar_pagos(prestamos):
    pagos = []
    pago_id = 1

    pesos_mora_por_producto = {
        'Hipotecario':        [85, 8, 4, 2, 1],     # 15% de mora
        'Personal':           [63, 17, 9, 6, 5],    # 37% de mora
        'Vehicular':          [65, 17, 9, 5, 4],    # 32% de mora
        'Tarjeta de Crédito': [68, 16, 8, 5, 3],    # 32% de mora
    }

    for prestamo in prestamos:
        pesos = pesos_mora_por_producto[prestamo['producto']]
        num_pagos = random.randint(3, prestamo['plazo_meses'])
        for cuota in range(1, num_pagos + 1):
            dias_atraso = random.choices(
                [0, random.randint(1, 30), random.randint(31, 60),
                 random.randint(61, 90),
                 random.randint(91, 180)], weights=pesos
            )[0]
            pago = {
                'pago_id': pago_id,
                'prestamo_id': prestamo['prestamo_id'],
                'numero_cuota': cuota,
                'monto_cuota': round(prestamo['monto'] / prestamo['plazo_meses'], 2),
                'dias_atraso': dias_atraso,
                'estado': 'Al día' if dias_atraso == 0 else 'Atrasado'
            }
            pagos.append(pago)
            pago_id += 1
    return pagos


#Escritor / Writer

if __name__ == '__main__':
    clientes = generar_clientes(500)
    guardar_csv(clientes, 'datos/clientes.csv')
    print(f"Generados {len(clientes)} clientes")

    prestamos = generar_prestamos(clientes)
    guardar_csv(prestamos, 'datos/prestamos.csv')
    print(f"Generados {len(prestamos)} prestamos")

    pagos = generar_pagos(prestamos)
    guardar_csv(pagos, 'datos/pagos.csv')
    print(f"Generados {len(pagos)} pagos")





















































































