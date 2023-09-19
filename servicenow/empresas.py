from compartilhado import constantes as c, ambiente as a
from servicenow import objetos as o, metodos as m


def renner(numero):
    pagina, api, browser = m.obtem_pagina()

    login = o.Login(pagina, c.URL_RENNER, c.ID_USUARIO_RENNER, c.ID_SENHA_RENNER, a.USUARIO_RENNER, a.SENHA_RENNER)
    login.envia_formulario()

    chamado = o.Chamado(pagina, c.ID_ENTRADA_PESQUISA, c.ID_BOTAO_PESQUISA, numero)
    chamado.pesquisa()
    chamado.clica()
    imagem = chamado.captura()

    m.fecha_pagina(api, browser)

    return imagem


def dia(numero):
    pagina, api, browser = m.obtem_pagina()

    login = o.Login(pagina, c.URL_DIA, c.ID_USUARIO_DIA, c.ID_SENHA_DIA, a.USUARIO_DIA, a.SENHA_DIA)
    login.envia_formulario()

    chamado = o.Chamado(pagina, c.ID_ENTRADA_PESQUISA, c.ID_BOTAO_PESQUISA, numero)
    chamado.pesquisa()
    chamado.clica()
    imagem = chamado.captura()

    m.fecha_pagina(api, browser)

    return imagem
