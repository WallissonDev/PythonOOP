import json

frutas = {
    "frutas": [
        {
            "nome": "Maçã",
            "preco": 6.49
        },
        {
            "nome": "Banana",
            "preco": 5.99
        }
    ]
}

with open("frutas.json", "w", encoding="utf-8") as arq: # Encoding serve pra aceitar caracteres especiais
    json.dump(frutas, arq, indent=4, ensure_ascii = True) # Identação de 4 argumentos
    # ensure_ascii para aceitar certos caracteres especiais

