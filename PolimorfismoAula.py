import math
class Forma: # Classe Pai / Ancestral / Mãe

    def __init__(self):
        print('Construtor da Forma')

    def area(self):
        print('Área da forma')

    def perimetro(self):
        print('Perimetro da Forma')

    def descricao(self):
        print('Descrição da forma')

class Quadrado(Forma): # Chamamos isso de especifição da Classe Forma -> Estamos especializando-se em ser um Quadrado. Chama-se também SUBCLASSE.

    def __init__(self, lado): # Estamos sobrescrevendo o método init da classe base -> Forma, assim como área e perimetro.
        self.lado = lado # Um novo campo

    def area(self): # Como é Polimorfismo, o próprio objeto, vai ter uma forma diferente de executar o método área.
        return self.lado**2 # Aqui é a individualidade de Quadrado, sem essa definição separada, apareceria 'Area da forma'

    def perimetro(self):
        return self.lado * 4

class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

    def descricao(self):
        print('Descrição do círculo.')

circ = Circulo(3)
print(f'Área: {circ.area()}')
print(f'Perimetro: {circ.perimetro()}')
circ.descricao() # Especificado, tem sua própria descrição
quad = Quadrado(2)
quad.descricao() # Não especificado, pega o comportamento da Classe Pai -> Descrição da forma
print(f'Área: {quad.area()}')
print(f'Perimetro: {quad.perimetro()}')