from api.umbler.constantes import ORGANIZATION_ID
from api.umbler.utils import get

r = get(f'/v1/chats?organizationId={ORGANIZATION_ID}')

if r.ok:
    try:
        resposta = r.json()
        for item in resposta['items']:
            print('Nome:'.ljust(10), item['contact']['name'])
            print('Id:'.ljust(10), item['id'], '\n\n')

    except:
        print('Não é JSON')
        print('Texto:')
        print(r.text)
else:
    print('Erro', r.status_code, ':', r.text)


a = r.json()
pass


