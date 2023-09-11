import json
import requests


with open('exemplo.json') as f:
    exemplo = json.load(f)


url_webhook = 'http://127.0.0.1:5000/webhook'

r = requests.post(url_webhook, json=exemplo)

print(r)