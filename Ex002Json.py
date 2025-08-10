import json

def json_exec(arquivo: str, tipo: any=None):
    """ Carrega um JSON ou cria se não existir """
    try:
        with open(arquivo, 'r') as arq:
            try:
                json.load(arquivo)
            except json.JSONDecodeError:
                print('Não existe, criando arquivo...')

    except FileNotFoundError:
        print(f'O arquivo : {arquivo} não foi encontrado, criando novo.')

    with open(arquivo, 'w') as arq:
        if tipo is None:
            padrao = {}
        json.dump(padrao, arq, indent=2)
    return padrao



