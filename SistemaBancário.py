class Cliente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self._cpf = None
        self.cpf = cpf

    @property
    def cpf(self):
        if len(self._cpf) == 11:
            self._cpf = str(self._cpf)
            return f"{self._cpf[:3]}.{self._cpf[3:6]}.{self._cpf[6:9]}-{self._cpf[9:]}"
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        cpf_str = str(valor)
        cpf_limpo = ''.join(cpf_str)
        self._cpf = cpf_limpo

class ContaBancaria:

    def __init__(self, numero, titular: Cliente, saldo = 0.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor <= 0:
            return False
        if valor <= self._saldo + self._limite_especial:
            self._saldo -= valor
            return True
        return False

    @property
    def numero(self):
        return f'Número da conta -> {self._numero}'

    @property
    def titular(self):
        return f'Titular da conta -> {self._titular}'

    @property
    def saldo(self):
        return f'Saldo Atual -> R$ {self._saldo}'

class ContaCorrente(ContaBancaria):

    def __init__(self, numero, titular, saldo, limite_especial = 100.0):
        super().__init__(numero, titular, saldo)
        self._limite_especial = limite_especial

    def sacar(self, valor):
        if valor > 0 and valor <= self.limite_total:
            self._saldo -= valor
            return True
        return False

    @property
    def limite_especial(self):
        return f' Limite Especial -> {self._limite_especial}'

    @limite_especial.setter
    def limite_especial(self, novo_limite):
        if novo_limite >= 0:
            self._limite_especial = novo_limite
        else:
            print('Erro: Limite não pode ser negativo')

    @property
    def limite_total(self):
        return self._saldo + self._limite_especial

class ContaPoupanca(ContaBancaria):

    def __init__(self, numero, titular, saldo = 0, taxa = 0.05):
            super().__init__(numero, titular, saldo)
            self._taxa = taxa

    @property
    def taxa_rendimento(self):
        return self._taxa

    @taxa_rendimento.setter
    def taxa_rendimento(self, nova_taxa):
        if 0 <= nova_taxa <= 1:
            self._taxa = nova_taxa
        else:
            print(f'Erro: Taxa deve ser entre 0 e 1')

    def aplicar_rendimento(self):
        rendimento = self._saldo * self._taxa
        self._saldo += rendimento
        return rendimento

class Banco:

    def __init__(self, nome: Cliente, lista_clientes = None):
        self.nome = nome
        self.tipo_conta = None
        self.lista_clientes = []












