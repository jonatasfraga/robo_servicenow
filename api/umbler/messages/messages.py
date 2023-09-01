import requests

url = "https://app-utalk.umbler.com/api/v1/messages/"

payload = {'Message': 'teste',
           'OrganizationId': 'ZNZiWiFuNRc6abTT',
           'ChatId': 'ZNZovyd0XXjqBUEt'}

headers = {
    'Authorization': 'Bearer E1FF0A94FF1FE462763EEB5D1C7E1001534175B928F4F0CEEB9AECFAB48DE6C6',
    # 'Content-Type': 'multipart/form-data'
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)
