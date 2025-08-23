class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def resetar(self): # Método/Função - Resetar -> Métodos tem um argumento obrigatório -> Self
        self.x = 0
        self.y = 0

    def mover(self, x, y):
        self.x = x
        self.y = y

"""
    p = Ponto(10,20) # p é um objeto
    print(p.x, p.y)
    Ponto.resetar(p)
    print(p.x, p.y)
"""
p = Ponto()
p.resetar()
print(p.x, p.y)
p.mover(10,20)
print(p.x, p.y)