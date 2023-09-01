from datetime import datetime as dt
from datetime import timedelta as td
from datetime import timezone as tz

from api.umbler.constantes import CHAT_ID, ORGANIZATION_ID
from api.umbler.utils import get

ultima_24_horas = (dt.now(tz.utc) - td(hours=24)).strftime('%Y-%m-%dT%H:%M:%S.%f')

r = get(f'/v1/chats/{CHAT_ID}/relative-messages/?'
        f'organizationId={ORGANIZATION_ID}&'
        f'FromEventUTC={ultima_24_horas}&'
        f'Take=250&'
        f'Direction=TakeBefore')

if r.ok:
    try:
        resposta = r.json()
        print(resposta)
        for mensagem in resposta['messages']:
            print('*' * 20)
            print('MENSAGEM EM:', mensagem['eventAtUTC'])
            print('CONTEUDO: ', mensagem['content'])
            print("\n\n\n\n")


    except:
        print('Não é JSON')
        print('Texto:')
        print(r.text)
else:
    print('Erro', r.status_code, ':', r.text)
