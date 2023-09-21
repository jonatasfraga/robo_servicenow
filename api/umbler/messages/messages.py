from api.umbler.utils import post


def envia_mensagem(mensagem, organizacao_id, chat_id):
    dados = {'Message': mensagem,
             'OrganizationId': organizacao_id,
             'ChatId': chat_id}
    caminho = '/api/messages'

    response = post(dados, caminho)

    print(response.text)
