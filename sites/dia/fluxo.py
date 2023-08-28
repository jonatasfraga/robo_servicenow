from sites.constantes import USUARIO_DIA, SENHA_DIA, ID_USUARIO_DIA, ID_SENHA_DIA, URL_DIA
from sites.login import Login
from sites.utilitarios import obtem_pagina


def fluxo_dia():
    pagina, p, browser = obtem_pagina()

    login = Login(pagina, URL_DIA, ID_USUARIO_DIA, ID_SENHA_DIA, USUARIO_DIA, SENHA_DIA)
    login.envia_formulario()
