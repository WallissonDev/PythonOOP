class Produto:

    def __init__(self, id, nome, preco):
        self._id = id
        self._nome = nome
        self._preco = preco

    def calcular_desconto(self, percentual):
        return self._preco * percentual / 100

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self._preco = valor
        else:
            print('O produto não pode custar menos que 0')

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return f'Nome: {self._nome} - ID: {self._id} - R$ {self._preco:.2f}'

class Livro(Produto):

    def __init__(self,id, nome, preco, autor, num_paginas):
        super().__init__(id, nome, preco)
        self._autor = autor
        self._num_paginas = num_paginas

    @property
    def autor(self):
        return self._autor

    @property
    def num_paginas(self):
        return self._num_paginas

    def __str__(self):
        return f'{super().__str__()} - Autor: {self._autor} - Páginas: {self._num_paginas}'

class Eletronico(Produto):

    def __init__(self, id, nome, preco, voltagem, fabricante):
        super().__init__(id, nome, preco)
        self._voltagem = voltagem
        self._fabricante = fabricante

    @property
    def voltagem(self):
        return self._voltagem

    @voltagem.setter
    def voltagem(self, nova_voltagem):
        if nova_voltagem in [110, 220, 'bivolt']:
            self._voltagem = nova_voltagem
        else:
            raise ValueError('Voltagem deve ser 110V, 220V ou Bivolt')

    @property
    def fabricante(self):
        return self._fabricante

    def __str__(self):
        return f'{super().__str__()} Voltagem: {self._voltagem} - Fabricante: {self._fabricante}'

class Catalogo:

    def __init__(self):
        self._lista = []

    def adicionar_produto(self, produto):
        if any(p.id == produto.id for p in self._lista):
            print(f'Produto ID:{produto.id} já está na lista!')
            return False
        self._lista.append(produto)
        return True

    def listar_todos(self):
        for p in self._lista:
            print(f'ID: {p.id} - NOME: {p.nome} - PREÇO: R$ {p.preco}')

    def buscar_produto(self, criterio, arg):
        for p in self._lista:
            if criterio == 'id':
                if p.id == arg:
                    return print(f'Produto encontrado na posição -> {self._lista.index(p)}')
            if criterio == 'nome':
                if p.nome == arg:
                    return print(f'Produto encontrado na posição -> {self._lista.index(p)}')
        return False

    def remover_produto(self, criterio, arg):
        for p in self._lista:
            if criterio.lower() == 'id' or criterio.lower() == 'nome':
                if p.nome == arg:
                    return self._lista.remove(p)
                elif str(p.id) == str(arg):
                    return self._lista.remove(p)
        return False

um2 = Livro( 1,'Livro das Revelações', 150, 'José', 250)
um3 = Livro( 2,'Biblia', 50, 'Cristo', 400)
um4 = Eletronico(3, 'Geladeira', 3000, 'bivolt', 'Brastemp')
cat = Catalogo()
cat.adicionar_produto(um2)
cat.adicionar_produto(um3)
cat.adicionar_produto(um4)
cat.buscar_produto('nome', 'Biblia')
cat.buscar_produto('id', 1)
cat.remover_produto('id', 2)
cat.listar_todos()
