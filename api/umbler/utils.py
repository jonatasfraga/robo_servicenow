import requests

from compartilhado.ambiente import AUTH
from compartilhado.constantes import HOST_UMBLER


def get(path):
    url = HOST_UMBLER + path
    headers = {'Authorization': AUTH, 'Content-Type': 'application/json'}
    return requests.get(url, headers=headers)


def post(path, body):
    url = HOST_UMBLER + path
    headers = {'Authorization': AUTH, 'Content-Type': 'application/json'}
    return requests.post(url, headers=headers, json=body)
