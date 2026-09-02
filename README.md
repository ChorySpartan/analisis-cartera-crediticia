# Análisis de Cartera Crediticia

Portafolio de análisis de datos aplicado al sector bancario guatemalteco, 
simulando cartera crediticia, mora y comportamiento de pago de clientes.

## Contexto

Proyecto simulado para practicar el flujo completo de un analista de datos 
en banca: generación de datos, limpieza, análisis en SQL, y próximamente 
visualización en Excel/Power BI.

## Herramientas utilizadas
- **SQL (SQLite)** — consultas de análisis: JOIN múltiples, GROUP BY, 
  HAVING, CASE WHEN, subconsultas, funciones de ventana (RANK, PARTITION BY)
- **Python (Faker, pandas)** — generación de datos simulados y limpieza 
  de calidad de datos
- **Excel / Power BI** — dashboards (próximamente)

## Estructura del proyecto
- `generar_datos.py` — generación de 500 clientes, préstamos y pagos 
  simulados con Faker
- `limpieza_analisis.py` — limpieza de datos con pandas (nulos, duplicados)
- `datos/` — archivos CSV generados
- `cartera.db` — base de datos SQLite con clientes, préstamos y pagos

## Hallazgos principales (hasta ahora)
- Mora general de la cartera: ~30%
- El segmento de empresarios con productos hipotecarios muestra la mora 
  más alta (32.6%)
- Los productos vehiculares e independientes también muestran mora por 
  encima del promedio
