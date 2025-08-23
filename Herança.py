class MinhaClasse(object):
    pass

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class PessoaFisica(Pessoa):

    def __init__(self, CPF, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.CPF = CPF

class PessoaJuridica(Pessoa):

    def __init__(self, CNPJ, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.CNPJ = CNPJ

p1 = Pessoa('Marcos', 28)
p_Fisica = PessoaFisica(6023232, 'Marcos', 28)