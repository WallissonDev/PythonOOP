class Produto:

    def __init__(self, nome, preço, quantia):
        self.nome = nome
        self.preço = preço
        self.quantia = quantia

    def valor_total(self):
        vt = self.quantia * self.preço
        return print(f'Valor total em estoque: R$ {vt}')

    def disponibilidade(self):
        if self.quantia >= 1:
            return print(f'{self.quantia} Produtos disponíveis.')
        else:
            return print(f'Produto indisponível')

p1 = Produto('Pasta', 2.5, 100)
p1.valor_total()
p1.disponibilidade()

p2 = Produto('Mesa', 500, 0)
p2.valor_total()
p2.disponibilidade()
