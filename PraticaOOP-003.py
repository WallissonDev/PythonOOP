class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        a = self.largura * self.altura
        return print(f'A área é {a}')

    def perimetro(self):
        p = 2 * (self.largura + self.altura)
        return print(f'O perimetro é {p} ')

r1 = Retangulo(7, 3)
r1.area()
r1.perimetro()