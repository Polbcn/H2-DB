import pandas as pd
import psycopg2

# Conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="H2-lab",
    user="admin",
    password="adminpsswd"
)

# Lista de tablas a exportar
tablas = ["sensores", "mediciones"]

# Crear un archivo Excel
writer = pd.ExcelWriter("exportado.xlsx", engine="xlsxwriter")

for tabla in tablas:
    df = pd.read_sql(f"SELECT * FROM {tabla}", conn)
    df.to_excel(writer, sheet_name=tabla, index=False)

writer.close()
conn.close()

print("Exportación completada: exportado.xlsx")
