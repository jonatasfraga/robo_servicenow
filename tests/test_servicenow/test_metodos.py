from os import environ as env

from compartilhado import constantes as c
from servicenow import metodos as m

NUMERO_CHAMADO_RENNER = env.get('NUMERO_CHAMADO_RENNER')
NUMERO_CHAMADO_DIA = env.get('NUMERO_CHAMADO_DIA')

casos = [
    (c.RENNER, NUMERO_CHAMADO_RENNER),
    (c.DIA, NUMERO_CHAMADO_DIA)
]


def obtem_captura_das_empresas(casos):
    for empresa, numero in casos:
        imagem = m.obtem_captura(empresa, numero)
        print(imagem, "\n\n\n\n")


if __name__ == '__main__':
    obtem_captura_das_empresas(casos)
