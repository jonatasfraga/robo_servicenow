import requests
import urllib.parse

from api.umbler.constantes import HOST, AUTH


def get(path):
    url = HOST + path
    headers = {'Authorization': AUTH, 'Content-Type': 'application/json'}
    return requests.get(url, headers=headers)


def post(path, body):
    url = HOST + path
    headers = {'Authorization': AUTH, 'Content-Type': 'application/json'}
    return requests.post(url, headers=headers)