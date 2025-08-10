import json

json_box = '''
{
    "livros":[
    {
        "titulo": "A Revolução dos Bichos",
         "autor": "George Orwell",
         "ano_publicacao": 1945,
         "genero": "Ficção Política",
         "editora": "Companhia das Letras"
         },
         {
         "titulo": "1984",
         "autor": "George Orwell",
         "ano_publicacao": 1949,
         "genero": "Ficção distópica",
         "editora": "Companhia das Letras"
      } 
    ]
}
'''

dados_json = json.loads(json_box)
for item in dados_json["livros"]:
    print(f'Nome: {item["titulo"]} - Autor: {item["autor"]}')
