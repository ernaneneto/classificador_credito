from flask import Flask, request, jsonify
import pandas as pd
from main import modelo_ia, engine

app = Flask(__name__)

@app.route('/analisar', methods=['POST'])
def analisar_credito():
    # O banco envia os dados via JSON (WebService)
    dados_recebidos = request.get_json()
    
    nome = dados_recebidos.get('nome')
    renda = dados_recebidos.get('renda')
    score = dados_recebidos.get('score')
    valor = dados_recebidos.get('valor')

    # 1. IA Processa o dado recebido via WebService
    entrada = pd.DataFrame([[renda, score]], columns=['renda', 'score'])
    predicao = modelo_ia.predict(entrada)
    status = "Aprovado" if predicao[0] == 1 else "Negado"

    # 2. Salva no Banco de Dados
    dados_final = pd.DataFrame([{
        'nome_cliente': nome,
        'renda_mensal': renda,
        'score_credito': score,
        'valor_emprestimo': valor,
        'resultado_ia': status
    }])
    dados_final.to_sql('analise_credito', con=engine, if_exists='append', index=False)

    # 3. Resposta do WebService (O sistema do banco recebe isso)
    return jsonify({
        "mensagem": "Análise realizada com sucesso",
        "cliente": nome,
        "status_aprovacao": status
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)