# Não Orientada a Objetos
from Ex001_Triangulos import triangulo

def menu():
    print('='*30)
    print(f'VERSÃO NAO - OOP '.center(30))
    print('='*30)
    print('0 - Encerrar')
    print('1 - Imprimir a relação de triangulos')
    print('2 - Imprimir um Triangulo especifíco')
    print('3 - Calcular a area total do terreno')
    print('-'*30)

lista = [[640,490,890]]
lista.append([890,410,920])
lista.append([920,400,580])
lista.append([580,380,300])
lista.append([400,430,250])

while True:
    menu()
    opc = int(input('Opcao: '))
    if opc == 0:
        break
    elif opc == 1:
        for i in range(len(lista)):
            triangulo.novo(lista[i][0], lista[i][1], lista[i][2])
            print('- Triangulo ', i + 1, '-')
            triangulo.imprimir()
    elif opc == 2:
        opc2 = int(input('Número do Triangulo: '))
        if opc2 <= 0 or opc2 > len(lista):
            print('ERRO: Triangulo não existe.')
            continue
        triangulo.novo(lista[opc2 - 1 ][0],lista[opc2 - 1 ][1],lista[opc2 - 1 ][2])
        print('- Triangulo', opc2, '-')
        triangulo.imprimir()
    elif opc == 3:
        area = 0.0
        for i in range(len(lista)):
            triangulo.novo(lista[i][0],lista[i][1],lista[i][2])
            area += triangulo.area()
        print(f'Area total do terreno: {area}')
