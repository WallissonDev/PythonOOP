import triangulo

def menu():
    print('='*30)
    print(f'VERSÃO NAO - OOP '.center(30))
    print('='*30)
    print('0 - Encerrar')
    print('1 - Imprimir Triangulo')
    print('2 - Criar um Triangulo Padrao de Pitagoras')
    print('3 - Criar um Triangulo Personalizado')

while True:
    menu()
    esc = int(input('Escolha: '))
    if esc == 0:
        break
    if esc == 1:
        triangulo.imprimir()
    if esc == 2:
        pass
    if esc == 3:
        l1 = int(input('Lado1 = '))
        l2 = int(input('Lado2 = '))
        l3 = int(input('Lado3 = '))
        triangulo.novo(l1,l2,l3)
        triangulo.imprimir()
