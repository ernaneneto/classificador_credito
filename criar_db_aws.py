import mysql.connector
import os
from dotenv import load_dotenv

# Carrega as variáveis do seu .env (que já tem o endpoint da AWS)
load_dotenv()

try:
    print("Conectando ao servidor AWS...")
    # Conecta ao servidor SEM especificar o banco de dados
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    
    cursor = conexao.cursor()
    
    # Cria o banco de dados
    print("Criando banco 'cooperativa_db'...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS cooperativa_db")
    
    print("✅ Sucesso! Banco de dados criado na AWS.")
    
    cursor.close()
    conexao.close()

except Exception as e:
    print(f"❌ Erro: {e}")