# Análisis de Cartera Crediticia

Portafolio de análisis de datos aplicado al sector bancario guatemalteco, 
simulando cartera crediticia, mora y comportamiento de pago de clientes.

## Contexto

Proyecto simulado para practicar el flujo completo de un analista de datos
en banca: generación de datos, limpieza, análisis en SQL, y próximamente
visualización en Excel/Power BI.

Los datos son 100% simulados; la relación entre tipo de producto y tasa de
mora fue diseñada intencionalmente para reflejar patrones de riesgo
crediticio realistas.

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

## Hallazgos principales

- Mora general de la cartera: **29.5%**
- El patrón de mora está directamente relacionado con la existencia de una garantía real:
  - **Hipotecario (14.4%)** — la mora más baja de la cartera. Al tener la vivienda como
    garantía, el cliente prioriza el pago para no perderla.
  - **Personal (37.1%)** — la mora más alta. Al ser créditos sin garantía real en la
    mayoría de los casos, representan el mayor riesgo de la cartera.
  - **Vehicular (34.9%)** — mora alta, aunque ligeramente menor que personal, consistente
    con contar con el vehículo como garantía parcial.
  - **Tarjeta de Crédito (31.7%)** — mora por encima del promedio general, en línea con
    el perfil de riesgo típico de este producto.
- Este patrón es consistente con la lógica de riesgo crediticio observada en la práctica:
  a mayor garantía real de por medio, menor probabilidad de atraso en el pago.