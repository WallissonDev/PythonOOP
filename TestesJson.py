import json

class Clima:
    def __init__(self, cidade_nome):
        self.cidade_nome = cidade_nome

    def aplicar_api(self, nome_arquivo: str):
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                try:
                    arquivo_carregar = json.load(arquivo)
                except json.JSONDecodeError:
                    print('ERRO ao carregar o arquivo.')
        except FileNotFoundError:
            print('Arquivo não encontrado.')

    def criar_json(self, valor_api: str, nome_arquivo: str):
            padrao = {
                "apikey": [
                    {
                        "apikey": f"{valor_api}"
                    }
                ]
            }
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(padrao, arquivo, indent=4)
            return padrao

canoas = Clima("Canoas")
canoas.criar_json("c9a42a06c0b743efcba8ae6f4713579e", "apikey.json")