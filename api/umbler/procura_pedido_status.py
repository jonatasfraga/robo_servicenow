from datetime import datetime as dt
from datetime import timedelta as td
from datetime import timezone as tz

import charset_normalizer.constant

from api.umbler.ambiente import CHAT_ID, ORGANIZATION_ID
from api.umbler.resposta_erro import resposta_erro
from api.umbler.utils import get
from servicenow.compartilhado.constantes import EMPRESAS

ultima_24_horas = (dt.now(tz.utc) - td(hours=10)).strftime('%Y-%m-%dT%H:%M:%S.%f')


def obtem_pedido_status():

    r = get(f'/v1/chats/{CHAT_ID}/relative-messages/?'
            f'organizationId={ORGANIZATION_ID}&'
            f'FromEventUTC={ultima_24_horas}&'
            f'Take=250&'
            f'Direction=TakeAfter')

    erros = {}
    requisicoes = {}

    if r.ok:
        resposta = r.json()
        for posicao, mensagem in enumerate(resposta['messages']):
            conteudo = mensagem['content']
            hora = mensagem['eventAtUTC']
            id_req = mensagem['id']

            if conteudo and 'STATUS_REQ' in conteudo:
                status_info = conteudo.split()
                if len(status_info) > 3:
                    erros.setdefault(id_req, []).append('nao enviado empresa ou numero')

                else:
                    empresa = status_info[1]
                    numero = status_info[2]

                    if empresa not in EMPRESAS:
                        erros.setdefault(id_req, []).append(f'empresa nao esta em: {EMPRESAS}')

                    else:
                        requisicoes[id_req] = {
                            'empresa': empresa,
                            'numero': numero
                        }

            elif conteudo and 'STATUS_RES' in conteudo:
                status_info = conteudo.split()
                if len(status_info) > 4:
                    id_req = status_info[3]
                    if id_req in requisicoes.keys():
                        requisicoes.pop(id_req)

                    if id_req in requisicoes.keys():
                        erros.pop(id_req)

            else:
                print('mensagem', posicao, 'fora do padrao')

        for erro in erros:
            resposta_erro(erro)

        return requisicoes


    else:
        print('Erro', r.status_code, ':', r.text)

        return []

