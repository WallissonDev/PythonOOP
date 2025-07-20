from math import pi

class Circulo:

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        calc = self.raio * self.raio
        return calc * pi

    def perimetro(self):
        perm = 2 * pi * self.raio
        return perm

circ = Circulo(5)
print(circ.area())
print(circ.perimetro())