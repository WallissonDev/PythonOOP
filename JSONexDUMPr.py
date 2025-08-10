import json

with open("frutas.json", "r") as arq:
    dados = json.load(arq)

for item in dados["frutas"]:
    print(item["preco"])
