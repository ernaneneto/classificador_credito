import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from dotenv import load_dotenv
import mysql.connector
from sqlalchemy import create_engine
import os


#Conexão Banco de Dados
load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
db = os.getenv("DB_NAME")

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db}')

#Simulando dados para Treinar a IA
#Aqui estou ensinando a IA o que é um bom pagador
dados_treino = {
    'renda': [2000, 5000, 1500, 8000, 3000, 10000],
    'score': [300, 700, 200, 900, 450, 950],
    'aprovado': [0, 1, 0, 1, 0, 1] # 0 = Negado, 1 = Aprovado
}

df_treino = pd.DataFrame(dados_treino)

#Modelo de IA (Árvore de Decisão)
modelo_ia = DecisionTreeClassifier()
modelo_ia.fit(df_treino[['renda', 'score']], df_treino['aprovado'])

print("IA Treinada com sucesso!")

#Processando novos Clientes
novos_clientes = [
    {'nome': 'João Silva', 'renda': 4500, 'score': 650, 'valor': 10000},
    {'nome': 'Maria Souza', 'renda': 1200, 'score': 250, 'valor': 5000},
    {'nome': 'Carlos Oliveira', 'renda': 7000, 'score': 800, 'valor': 20000}
]

#Processando Análise
def processar_analise():
    print("Iniciando processamento de crédito...")

    for cliente in novos_clientes:
        dados_para_prever = pd.DataFrame([[cliente['renda'], cliente['score']]], columns=['renda', 'score'])
        predicao = modelo_ia.predict(dados_para_prever)

        status = "Aprovado" if predicao[0] == 1 else "Negado"
        if status == "Negado" and cliente["renda"] > 3000:
            status = "Revisão Manual" #Minimiza o risco de perder bom cliente
        
        #Preparando dado para o Banco de Dados
        dados_final = pd.DataFrame([{
            'nome_cliente': cliente['nome'],
            'renda_mensal': cliente['renda'],
            'score_credito': cliente['score'],
            'valor_emprestimo': cliente['valor'],
            'resultado_ia': status
        }])

        dados_final.to_sql('analise_credito', con=engine, if_exists='append', index=False)
        print(f"Cliente {cliente['nome']} processado: {status}")

if __name__ == "__main__":
    processar_analise()