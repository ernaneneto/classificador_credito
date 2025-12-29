import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#Conexão com Banco de Dados
load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
db = os.getenv("DB_NAME")

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db}')

#Executando RPA
def executar_rpa():
    print("🤖 Iniciando Robô de Automação (RPA)...")

    #Robô buscando apenas os aprovados pela IA
    query = "SELECT * FROM analise_credito WHERE resultado_ia = 'Aprovado'"
    df_aprovados = pd.read_sql(query, con=engine)

    if not df_aprovados.empty:
        #Gera relatório
        nome_arquivo = 'relatorio_final_financeiro.xlsx'
        df_aprovados.to_excel(nome_arquivo, index=False)

        print(f"✅ Sucesso! O Robô gerou o arquivo '{nome_arquivo}' com {len(df_aprovados)} registros.")
        print(f"📂 Caminho: {os.path.abspath(nome_arquivo)}")
    else:
        print("⚠️ Nenhum registro aprovado para exportar hoje.")

if __name__ == "__main__":
    executar_rpa()