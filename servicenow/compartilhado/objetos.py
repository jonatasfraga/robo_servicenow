import time
from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass
class Pesquisa:
    pagina: Page
    entrada_id: str
    botao_id: str
    numero: str

    def preenche_entrada(self):
        print('PREENCHENDO ENTRADA PESQUISA')
        self.pagina.fill('#' + self.entrada_id, self.numero)
        time.sleep(5)

        self.pagina.click('#' + self.botao_id)


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
        self.pagina.fill('#' + self.usuario_id, self.usuario)
        self.pagina.fill('#' + self.senha_id, self.senha)
        time.sleep(5)

        self.pagina.keyboard.press('Enter')

        return True
