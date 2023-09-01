from servicenow.compartilhado import objetos as o
from servicenow.compartilhado import metodos as m
from servicenow.compartilhado import constantes as c
from servicenow.compartilhado import ambiente as a
from servicenow import fluxos as f

if __name__ == '__main__':

    print('INICIO FLUXO ' + a.FLUXO)

    if a.FLUXO == c.DIA:
        f.dia()

    if a.FLUXO == c.RENNER:
        f.renner()
