from sites.constantes import USUARIO_RENNER, SENHA_RENNER, ID_USUARIO_RENNER, ID_SENHA_RENNER, URL_RENNER
from sites.login import Login
from sites.utilitarios import obtem_pagina


def fluxo_renner():
    pagina, p, browser = obtem_pagina()

    login = Login(pagina, URL_RENNER, ID_USUARIO_RENNER, ID_SENHA_RENNER, USUARIO_RENNER, SENHA_RENNER)
    login.envia_formulario()

    pass
