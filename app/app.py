from flask import Flask, request, jsonify

from api.umbler.messages.messages import envia_mensagem
from compartilhado import ambiente as a
from compartilhado import constantes as c
from servicenow.metodos import obtem_captura

app = Flask(__name__)


@app.after_request
def response_processor(response):
    @response.call_on_close
    def process_after_request():
        empresa = response.json['Data']['empresa']
        numero_chamado = response.json['Data']['numero_chamado']
        chat_id = response.json['Chat']['Id']

        imagem = obtem_captura(empresa, numero_chamado)

        envia_mensagem(imagem, a.ORGANIZATION_ID, chat_id)

        print(empresa, numero_chamado)

    return response


@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()

    chat_id = json_data.get('Chat', {}).get('Id')

    escolha_empresa = json_data.get('Data', {}).get(f'{a.ID_ENTRADA_EMPRESA}:raw')
    empresa = c.ID_EMPRESAS_DICIONARIO[escolha_empresa]

    numero_chamado = json_data.get('Data', {}).get(f'{a.ID_ENTRADA_NUMERO_CHAMADO}:raw')

    print(empresa, numero_chamado)

    retorno = {
        'Data': {
            'numero_chamado': numero_chamado,
            'empresa': empresa,
            'status': 'pesquisando',
            'chat_id': chat_id,
        }
    }
    return jsonify(retorno)
