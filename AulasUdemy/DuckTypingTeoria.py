# "Se um objeto anda como um pato e faz quack como um pato, então ele é um pato."
# Programe para as interfaces, não para uma implementação.
"""
class Pato:

    def quack(self):
        print('Quack!!')

class Pessoa:

    def quack(self):
        print('QUACK!!!')

def na_floresta(arg):
        arg.quack()

na_floresta(Pato())
na_floresta(Pessoa())
"""
"""
class Livro:

    def __init__(self, titulo, lancamento, autor):
        self.titulo = titulo
        self.lancamento = lancamento
        self.autor = autor

class Filme:

    def __init__(self, titulo, lancamento, diretor):
        self.titulo = titulo
        self.lancamento = lancamento
        self.diretor = diretor

def imprimir(midia):
    print(midia.titulo, midia.lancamento)
"""

class Pato:

    def quack(self):
        print('Quack!')

class Pessoa:

    def quack(self):
        print('Faço quack como um pato!')

# Isso não é Pythonico
"""
def fazer_quack(obj):

    if isinstance(obj, Pato):
        obj.quack()
    else:
        print('Isso tem que ser um pato!')
"""
"""
# Não Pythonico
def fazer_quack(obj):
    # LBYL -> Estilo de Codifição
    if hasattr(obj, 'quack'):
        if callable(obj.quack):
            obj.quack()
"""
# ESSE É PYTHONICO
def fazer_quack(obj):
    # EAFP -> Easier to ask for forgiveness than permission.
    try:
        obj.quack()
    except AttributeError as e:
        print(e)

pat = Pato()
fazer_quack(pat)
pess = Pessoa()
fazer_quack(pess)



















