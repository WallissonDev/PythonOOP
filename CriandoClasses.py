#class MinhaClasse():
#    pass

#obj = MinhaClasse()
#print(obj)
class Ponto:

    def resetar(self): # Método do Objeto
        self.x = 0 # X é um atributo
        self.y = 0 # Y é um atributo


p = Ponto() # Atribuimos a variável P a class Ponto
p.resetar() # Chamamos o método pela variável
print(p.x, p.y) # Usamos os métodos pra chamar os atributos