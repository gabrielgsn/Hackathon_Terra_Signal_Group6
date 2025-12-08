from databricks.sdk import WorkspaceClient
import os

# Suas credenciais manuais (já que vai rodar no VSCode)
SERVER_HOSTNAME = "dbc-0e3f07fe-e650.cloud.databricks.com"
ACCESS_TOKEN = "dapid8c060e9eb73cce9fbf561016496d6e7"

print("🔍 Buscando modelos disponíveis...")

try:
    w = WorkspaceClient(host=f"https://{SERVER_HOSTNAME}", token=ACCESS_TOKEN)
    
    endpoints = w.serving_endpoints.list()
    
    print("\n--- MODELOS DISPONÍVEIS ---")
    found = False
    for item in endpoints:
        # Filtra apenas os que são Foundation Models ou LLMs
        if 'instruct' in item.name or 'chat' in item.name or 'dbrx' in item.name:
            print(f"✅ Nome para usar no código: {item.name}")
            found = True
            
    if not found:
        print("⚠️ Nenhum modelo de chat/instruct encontrado. Liste todos:")
        for item in endpoints:
            print(f"Nome: {item.name} (Tipo: {item.task})")

except Exception as e:
    print(f"Erro: {e}")