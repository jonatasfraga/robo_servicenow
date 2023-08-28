from sites.constantes import DIA, FLUXO, RENNER
from sites.dia.fluxo import fluxo_dia
from sites.renner.fluxo import fluxo_renner

if __name__ == '__main__':

    print('INICIO FLUXO ' + FLUXO)

    if FLUXO == DIA:
        fluxo_dia()

    if FLUXO == RENNER:
        fluxo_renner()
