import os

from playwright.sync_api import sync_playwright

from compartilhado import constantes as c
from servicenow.empresas import renner, dia


def obtem_captura(empresa, numero):
    if empresa == c.RENNER:
        return renner(numero)

    if empresa == c.DIA:
        return dia(numero)


def obtem_pagina():
    api = sync_playwright().start()
    nao_abre_interface_grafica = not os.environ.get(c.INTERFACE_GRAFICA) == '1'
    navegador = api.chromium.launch(headless=nao_abre_interface_grafica)
    pagina = navegador.new_page()
    pagina.set_default_navigation_timeout(3 * 60 * 1000)

    return pagina, api, navegador


def fecha_pagina(api, browser):
    browser.close()
    api.stop()


def obtem_numero_da_fila():
    return None
