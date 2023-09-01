from api.umbler.utils import get

ME = '/v1/members/me'
j = 30
r = get(ME)

if r.ok:
    try:
        resposta = r.json()
        print('Nome Membro:'.ljust(j), resposta['displayName'])
        print('Email Membro:'.ljust(j), resposta['emailAddress'])
        print('Número Membro:'.ljust(j), resposta['cellphone'])
        print('Id Membro:'.ljust(j), resposta['id'])
        print('Id Umbler Membro:'.ljust(j), resposta['umblerAccountId'])

        organizacoes = resposta['organizations']

        for organizacao in organizacoes:
            print('ORGANIZACAO', organizacao['name'])
            print('\t ID:'.ljust(j), organizacao['name'])
            print('\t PERMISSOES:'.ljust(j), organizacao['permissions'])
    except:
        print('Não é JSON')
        print('Texto:')
        print(r.text)
else:
    print('Erro', r.status_code, ':', r.text)
