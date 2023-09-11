from flask import Flask, request
from compartilhado import ambiente as a
from compartilhado.constantes import ID_EMPRESAS_DICIONARIO

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()

    escolha_empresa = json_data.get('Data', {}).get(f'{a.ID_ENTRADA_EMPRESA}:raw')
    empresa = ID_EMPRESAS_DICIONARIO[escolha_empresa]

    numero_chamado = json_data.get('Data', {}).get(f'{a.ID_ENTRADA_NUMERO_CHAMADO}:raw')

    print(empresa, numero_chamado)

    return 'Hello, World!'
