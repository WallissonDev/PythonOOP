class Funcionario:

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def info(self):
        return print(f'Funcionário: {self.nome} / Salário: R$ {self.salario} / Cargo: {self.cargo}')

    def descontos_beneficios(self):
        vt = (self.salario * 6 / 100)
        va = (self.salario * 20 / 100)
        self.salario = self.salario - vt - va
        return print(f'Valor descontado VT = R$ {vt} / VA = R$ {va}\nValor do Salário pós descontos: R$ {self.salario}')

f1 = Funcionario('Wally', 2000, 'Monitor de Eventos')
f1.info()
f1.descontos_beneficios()
f1.info()