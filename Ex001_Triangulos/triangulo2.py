import math

def menu():
    print('='*30)
    print('Triangulo em OOP'.center(30))
    print('='*30)
    print('0 - Encerrar')
    print('1 - Imprimir Triangulo')
    print('2 - Criar um Triangulo Padrao de Pitagoras')
    print('3 - Criar um Triangulo Personalizado')
    print('='*30)

class Triangulo:

    lado1 = 0
    lado2 = 0
    lado3 = 0

    def limpa(self):
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        sp = self.perimetro() / 2
        return math.sqrt(sp * (sp-self.lado1)*(sp-self.lado2)*(sp-self.lado3))

    def imprimir(self):
        print(f'Lado 1 = {self.lado1} | Lado 2 = {self.lado2} | Lado3 = {self.lado3}')
        print(f'Perimetro = {self.perimetro()}')
        print(f'Area -> {self.area()}')
    
    def valido(self):
        return self.lado1 < self.lado2 + self.lado3 and self.lado2 < self.lado1 + self.lado3 and self.lado3 < self.lado1 + self.lado2

    def novo(self, l1, l2, l3):
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3
        if self.valido():
            return True
        return False
        