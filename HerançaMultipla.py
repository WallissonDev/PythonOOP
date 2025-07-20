class Funcionario:

    def __init__(self, nome, salario, cpf):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf

    def get_bonitificacao(self):
        return self.salario * 0.10

class Gerente(Funcionario):

    def __init__(self, nome, salario, cpf, senha):
        super().__init__(nome, salario, cpf)
        self.senha = senha

    def get_bonitificacao(self):
        return self.salario * 0.10 + 1000

g = Gerente('Wally', 1900, 123, 'abc123')
print(g.get_bonitificacao())
print(g.senha)