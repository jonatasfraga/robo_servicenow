import time
from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass
class Chamado:
    pagina: Page
    entrada_id: str
    botao_id: str
    numero: str

    def pesquisa(self):
        print('PREENCHENDO ENTRADA PESQUISA')
        self.pagina.locator('#' + self.entrada_id).click()
        time.sleep(5)
        self.pagina.keyboard.type(self.numero)
        time.sleep(5)
        self.pagina.click('#' + self.botao_id)

    def clica(self):
        time.sleep(5)
        self.pagina.click('li[data-testclass=sn-global-search-record]')

    def captura(self):
        time.sleep(5)
        import base64
        self.pagina.set_viewport_size({"height": 4000, "width": 500})
        screenshot_bytes = self.pagina.frame_locator('#gsft_main').locator(
            "div[data-position-below-header='true']").screenshot()
        return base64.b64encode(screenshot_bytes).decode()


@dataclass
class Login:
    pagina: Page
    url: str
    usuario_id: str
    senha_id: str
    usuario: str
    senha: str

    def envia_formulario(self):
        print('ENVIANDO FORMULÁRIO LOGIN')
        self.pagina.goto(self.url)
        time.sleep(5)
        self.pagina.fill('#' + self.usuario_id, self.usuario)
        self.pagina.fill('#' + self.senha_id, self.senha)
        time.sleep(5)

        self.pagina.keyboard.press('Enter')

        return True
