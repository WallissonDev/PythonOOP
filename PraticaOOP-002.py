class ContaBancária:

    def __init__(self, num, nome, saldo):
        self.num = num
        self.nome = nome
        self.saldo = saldo

    def deposito(self, quantia):
        return print(f'Foi depositado : R$ {quantia} = Total R$ {self.saldo + quantia}')

    def saque(self, quantia):
        return print(f'Foi retirado R$ {quantia} = Saldo R$ {self.saldo - quantia}')


pessoa1 = ContaBancária(123, 'Wallisson', 1000)
pessoa1.deposito(500)
pessoa1.saque(200)