import math

# Exemplificação de não orientada a objetos. 

lado1 = 0
lado2 = 0
lado3 = 0

def limpa():
    global lado1
    lado1 = 0
    global lado2
    lado2 = 0
    global lado3
    lado3 = 0

def imprimir():
    print(f'Lado 1-> {lado1} | Lado 2 -> {lado2} | Lado 3 -> {lado3}')
    print(f'Perimetro -> {perimetro()}')
    print(f'Area -> {area()}')


def perimetro():
    return lado1 + lado2 + lado3

def valido():
    return lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1

def area():
    s = perimetro() / 2
    return math.sqrt(s *( s - lado1) * ( s - lado2) * ( s - lado3))

def novo(l1,l2,l3):
    global lado1
    lado1 = l1
    global lado2
    lado2 = l2
    global lado3
    lado3 = l3

    if not valido():
        limpa()
        return False
    return True