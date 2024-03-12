import requests
import json
ts = 1
public_key = '158dca0d7d027a40162adad3476c6e2b'
private_key = '22e445f8570c94f8061d873e9f93a78125e6c362'
# 122e445f8570c94f8061d873e9f93a78125e6c362158dca0d7d027a40162adad3476c6e2b
hashed = 'f35d0b44757f69d50a2bbe6c9813a832'
url = f'https://gateway.marvel.com:443/v1/public/comics?ts={ts}&apikey={public_key}&hash={hashed}'

response = requests.get(url)
if response.status_code == 200:
    response_json = json.loads(response.text)
    print(response_json)
