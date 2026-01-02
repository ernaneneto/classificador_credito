import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# 1. Configuração de Estilo
st.set_page_config(page_title="Portal de Crédito - Cooperativa", layout="wide")

# CSS para remover menus desnecessários e melhorar fontes
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #1f77b4; }
    </style>
    """, unsafe_allow_html=True)

# Conexão Banco de Dados
load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
db = os.getenv("DB_NAME")

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db}')

try:
    # Busca e Tratamento de Dados
    df_raw = pd.read_sql("SELECT * FROM analise_credito", con=engine)
    
    # --- MELHORIA VISUAL: Renomeando colunas para o usuário ---
    df = df_raw.rename(columns={
        'nome_cliente': 'Nome do Cliente',
        'renda_mensal': 'Renda Mensal',
        'score_credito': 'Score de Crédito',
        'valor_emprestimo': 'Valor Solicitado',
        'resultado_ia': 'Decisão da IA',
        'data_processamento': 'Data da Análise'
    })

    st.title("🏦 Sistema Inteligente de Crédito")
    st.subheader("Monitoramento de Eficiência Operacional e IA")

    # Métricas
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total de Processos", f"{len(df)} itens")
    with m2:
        aprovados = len(df[df['Decisão da IA'] == 'Aprovado'])
        st.metric("Taxa de Aprovação", f"{(aprovados/len(df)*100):.1f}%")
    with m3:
        ticket = df['Valor Solicitado'].mean()
        st.metric("Valor Médio Solicitado", f"R$ {ticket:,.2f}")

    st.divider()

    # Layout de Gráficos
    c1, c2 = st.columns([1, 1.5]) # C2 é um pouco maior para o gráfico de dispersão

    with c1:
        st.markdown("### 📈 Resumo de Decisões")
        # Gráfico de barras horizontal
        contagem = df['Decisão da IA'].value_counts()
        st.bar_chart(contagem, color="#007bff")

    with c2:
        st.markdown("### 🎯 Perfil de Risco (Score vs Renda)")
        # Gráfico de dispersão
        st.scatter_chart(
            data=df, 
            x='Score de Crédito', 
            y='Renda Mensal', 
            color='Decisão da IA',
            size='Valor Solicitado' # O tamanho da bolinha indica o valor do empréstimo
        )

    # Tabela com formatação de moeda
    st.markdown("### 📋 Detalhamento das Propostas")
    st.dataframe(
        df.style.format({
            "Renda Mensal": "R$ {:.2f}",
            "Valor Solicitado": "R$ {:.2f}",
            "Data da Análise": lambda t: t.strftime("%d/%m/%Y %H:%M")
        }),
        use_container_width=True,
        hide_index=True
    )

except Exception as e:
    st.error(f"Erro: {e}")