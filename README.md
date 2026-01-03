## 🏦 Sistema Inteligente de Análise de Crédito

Este projeto simula um ecossistema financeiro completo: desde a entrada de dados via API, decisão por Inteligência Artificial, persistência em nuvem (AWS RDS), monitoramento por Dashboard e fechamento de processos via RPA.

## 🌐 Arquitetura da Solução

Diferente de projetos locais, esta solução utiliza uma arquitetura híbrida e distribuída:

* **Camada de Dados:** Instância gerenciada AWS RDS (MySQL) garantindo alta disponibilidade.
* **Inteligência:** Modelo de Classificação treinado com Scikit-Learn integrado à API.
* **Interface Cloud:** Dashboard hospedado no Streamlit Cloud para acesso remoto.
* **Integração:** API REST pronta para receber requisições de sistemas legados ou mobile.

## 🚀 Tecnologias Utilizadas
* **Cloud:** AWS RDS (Relational Database Service).
* **Linguagem:** Python 3.12+ (Ambiente isolado com `venv`)
* **IA/ML:** Scikit-Learn (Decision Tree), Pandas.
* **Banco de Dados:** MySQL com SQLAlchemy (ORM).
* **API/Web:** Flask & Postman/Thunder Client.
* **Dashboard:** Streamlit
* **Automação (RPA):** Pandas & Openpyxl para geração de relatórios .xlsx.
* **Segurança:** Dotenv (Variáveis de Ambiente)=

## 🛠️ Funcionalidades
1. **Ingestão:** Os dados de crédito são enviados via JSON para o endpoint /analisar da API Flask.
2. **Processamento:** O motor de IA classifica a proposta como "Aprovado" ou "Reprovado".
3. **Persistência:** O resultado é gravado instantaneamente no banco de dados na AWS.
4. **Monitoramento:** O Dashboard consome os dados da nuvem e exibe métricas de risco e volume financeiro.
5. **RPA de Exportação:** Um robô de automação busca apenas os "Aprovados" no banco e gera o arquivo para o setor de pagamentos.
 
## 📋 Como Rodar
1. **Ambiente:** Crie o ambiente virtual `python -m venv venv`
2. **Instale as dependências:** `pip install -r requirements.txt`
3. **Variáveis de Ambiente:** Configure dotenv com seu `DB_HOST`(Endpoint AWS), `DB_USER` e `DB_PASSWORD` e `DB_NAME`, no arquivo `.env.example` 
4. **Treine o modelo:** `python main.py`
4. **API:** Inicie o serviço de recebimento `python api.py`
5. **Dashboard:** Para visualizar os gráficos `streamlit run dashboard.py`
6. **Execute o RPA:** Gere o relatório financeiro `python rpa_export.py`