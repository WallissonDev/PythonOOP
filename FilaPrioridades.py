import heapq

class FilaDePrioridade:

    def __init__(self):
        self.fila = []
        self.indice = 0

    def inserir(self, item, prioridade): # Chamamos Comumente de Push
        heapq.heappush(self.fila, (-prioridade, self.indice, item))
        self.indice += 1

    def remover(self): # Comumente Chamamos de Pop
        return heapq.heappop(self.fila)[-1]


class Item:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f'{self.nome}'

fila = FilaDePrioridade()
fila.inserir(Item('Marcos'), 28)
fila.inserir(Item('Joao'),30)
fila.inserir(Item('Maria'), 18)

print(fila.remover())
print(fila.remover())