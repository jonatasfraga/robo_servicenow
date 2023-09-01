from api.umbler.procura_pedido_status import obtem_pedido_status
from servicenow.compartilhado import constantes as c
from servicenow import fluxos as f
from time import sleep

if __name__ == '__main__':
    while 1:
        print("OBTENDO PEDIDOS")
        lista_pedidos = obtem_pedido_status()

        for id_mensagem, pedido in lista_pedidos.items():
            empresa = pedido.get('empresa')
            numero = pedido.get('numero')

            if empresa == c.DIA:
                f.dia(numero)

            if empresa == c.RENNER:
                f.renner(numero)

        sleep(60)
        print("AGUARDANDO 1 MINUTO")
