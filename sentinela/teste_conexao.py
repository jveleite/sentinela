from db import get_connection

try:
    conn = get_connection()
    print("Conexão com o banco estabelecida com sucesso!")
    conn.close()
    print("Conexão encerrada.")
except Exception as e:
    print(f"Erro ao conectar: {e}")