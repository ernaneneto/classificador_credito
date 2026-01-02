# 🏦 Sistema Inteligente de Análise de Crédito

Projeto desenvolvido para automatizar e otimizar o processo de análise de crédito em cooperativas, utilizando Inteligência Artificial, Banco de Dados Relacional, Dashboard e API REST.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.x (Ambiente isolado com `venv`)
* **IA/Machine Learning:** Scikit-Learn (Decision Tree Classifier)
* **Banco de Dados:** MySQL com SQLAlchemy
* **Framework Web:** Flask (WebService/API REST)
* **Dashboard:** Streamlit
* **Automação (RPA):** Pandas & Openpyxl
* **Segurança:** Dotenv (Variáveis de Ambiente)

## 🛠️ Funcionalidades
1. **Motor de IA:** Analisa renda e score para tomada de decisão automática.
2. **WebService (API):** Interface para integração com sistemas externos (App/Web) via JSON.
3. **Persistência:** Gravação de logs de análise em banco de dados SQL para conformidade e auditoria.
4. **Dashboard:** Visualização em tempo real de taxas de aprovação e métricas financeiras.
5. **RPA de Exportação:** Geração automática de relatórios em Excel para o departamento financeiro.

## 📋 Como Rodar
1. Configure o arquivo `.env.example` com suas credenciais do MySQL.
2. Instale as dependências: `pip install -r requirements.txt`
3. **Treine o modelo:** `python main.py`
4. **Inicie o WebService (API):** `python api.py`
5. **Inicie o dashboard:** `streamlit run dashboard.py`
6. **Execute o RPA:** `python rpa_export.py` (quando desejar gerar o relatório)