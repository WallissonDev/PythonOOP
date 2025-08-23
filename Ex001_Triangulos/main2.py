from triangulo2 import Triangulo, menu

tri = Triangulo()

while True:
    menu()
    esc = int(input('Escolha: '))
    if esc == 0:
        break
    if esc == 1:
        tri.imprimir()
    if esc == 2:
        tri.novo(5,7,10)
    if esc == 3:
        ld1 = int(input('Lado1 : '))
        ld2 = int(input('Lado2 : '))
        ld3 = int(input('Lado3 : '))
        if tri.novo(ld1,ld2,ld3):
            print('Criado com sucesso!')
        else:
            print('Triangulo inválido')