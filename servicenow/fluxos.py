from servicenow import objetos as o, metodos as m
from compartilhado import constantes as c, ambiente as a


def renner(numero):
    pagina, p, browser = m.obtem_pagina()

    login = o.Login(pagina, c.URL_RENNER, c.ID_USUARIO_RENNER, c.ID_SENHA_RENNER, a.USUARIO_RENNER, a.SENHA_RENNER)
    login.envia_formulario()

    pesquisa = o.Pesquisa(pagina, c.ID_ENTRADA_PESQUISA, c.ID_BOTAO_PESQUISA, numero)
    pesquisa.envia_formulario()
    pesquisa.clica_item()
    imagem = pesquisa.captura()

    return imagem


def dia(numero):
    pagina, p, browser = m.obtem_pagina()

    login = o.Login(pagina, c.URL_DIA, c.ID_USUARIO_DIA, c.ID_SENHA_DIA, a.USUARIO_DIA, a.SENHA_DIA)
    login.envia_formulario()

    pesquisa = o.Pesquisa(pagina, c.ID_ENTRADA_PESQUISA, c.ID_BOTAO_PESQUISA, numero)
    pesquisa.envia_formulario()
    pesquisa.clica_item()
    imagem = pesquisa.captura()

    return imagem
