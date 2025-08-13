import requests
import json

class Clima:
    def __init__(self, cidade_nome, arquivo_api=None, url=None):
        self.cidade_nome = cidade_nome
        self.arquivo_api = arquivo_api
        try:
            with open(arquivo_api, 'r', encoding='utf-8') as arquivo:
                try:
                    arquivo_carregar = json.load(arquivo)
                    self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.cidade_nome}&appid={arquivo_carregar["apikey"]}&units=metric&lang=pt"
                except json.JSONDecodeError:
                    print('ERRO ao carregar o arquivo. Tente Crialo com: criar_json')
        except FileNotFoundError:
            print('Arquivo não encontrado. Utilize método: criar_json("suaAPI", "NomeArquivo"')
            self.url = None

    def previsão(self):
        carregar_prev = requests.get(self.url)
        prep = carregar_prev.json()
        qualidade_ceu = prep["weather"][0]["description"]
        temperatura = prep["main"]["temp"]
        sensacao = prep["main"]["feels_like"]
        maxima = prep["main"]["temp_max"]
        minima = prep["main"]["temp_min"]
        print(f'Em {self.cidade_nome}: {qualidade_ceu} com a temperatura em {temperatura}°C maxima de {maxima}°C e mínima de {minima}°C com sensaçao de {sensacao}°C')

    def criar_json(self, valor_api: str, nome_arquivo: str):
            padrao = {
                        "apikey": f"{valor_api}"
                    }
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(padrao, arquivo, indent=4)
            return padrao

canoas = Clima("Canoas", "apikey.json")
sao_paulo = Clima("São Paulo", "apikey.json")
sao_paulo.previsão()
canoas.previsão()