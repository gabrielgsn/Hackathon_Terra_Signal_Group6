from databricks import sql

# --- SEUS DADOS ---
SERVER_HOSTNAME = "coloque seu hostname aqui"
HTTP_PATH = "/sql/1.0/warehouses/coloque seu http path aqui"
ACCESS_TOKEN = "coloque seu token aqui"

connection = sql.connect(server_hostname=SERVER_HOSTNAME, http_path=HTTP_PATH, access_token=ACCESS_TOKEN)
cursor = connection.cursor()

# Vamos olhar a tabela que parece ser a final
tabela_alvo = "workspace.default.churn_predictions_final"

print(f"👀 Espiando: {tabela_alvo}")
try:
    cursor.execute(f"SELECT * FROM {tabela_alvo} LIMIT 3")
    colunas = [desc[0] for desc in cursor.description]
    print(f"COLUNAS: {colunas}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print(e)

connection.close()