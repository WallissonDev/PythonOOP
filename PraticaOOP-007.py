class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def valido(self):
        if self.lado1 == self.lado2 == self.lado3:
            a = "Equilatereo"
            return print(f'É um triangulo {a}')
        elif self.lado1 == self.lado2 and self.lado1 != self.lado3:
            b = "Isoceles"
            return print(f'É um triangulo {b}')
        elif self.lado2 == self.lado3 and self.lado2 != self.lado1:
            b = "Isoceles"
            return print(f'É um triangulo {b}')
        elif self.lado3 == self.lado1 and self.lado3 != self.lado2:
            b = "Isoceles"
            return print(f'É um triangulo {b}')
        elif self.lado1 != self.lado2 != self.lado3:
            c = "Escaleno"
            return print(f'É um triangulo {c}')
        else:
            return print(f'Não é um Triangulo')

t1 = Triangulo(3,4,5)
t1.valido()
t2 = Triangulo(5, 5, 3)
t2.valido()
t3 = Triangulo(5,5,5)
t3.valido()
t4 = Triangulo(5, 8, 3)
t4.valido()