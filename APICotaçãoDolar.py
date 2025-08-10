import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
a = requisicao.json()
print(a['USDBRL']['bid'])