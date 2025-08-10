class Cliente:

    def __init__(self, nome, identificador, num_pessoas):
        self.nome = nome
        self.identificador =  identificador
        self.num_pessoas = num_pessoas

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, valor):
        if valor > 0:
            self._identificador = valor
        else:
            raise ValueError('Numero deve ser acima de 0')

    @property
    def num_pessoas(self):
        return self._num_pessoas

    @num_pessoas.setter
    def num_pessoas(self, num):
        if num > 0:
            self._num_pessoas = num
        else:
            raise ValueError('Deve ter no mínimo 1 pessoa!')


class Mesa:

    def __init__(self, numero, capacidade, disponivel = True):
        self.numero = numero
        self.capacidade = capacidade
        self.disponivel = disponivel

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, idmesa):
        if idmesa >= 0:
            self._numero = idmesa
        else:
            raise ValueError('Número Inválido')

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if valor > 0:
            self._capacidade = valor
        else:
            raise ValueError('Capacidade deve ser acima de 0')

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, valor):
        if valor in [True, 1, "Sim", "sim", "S", "s", "True"]:  
            self._disponivel = True
        elif valor in [False, 0, "Nao", "nao", "Não", "não", "N", "n", "False"]:
            self._disponivel = False
        else:
            raise ValueError(f"Valor inválido para disponível: {valor}")

class Restaurante:

    def __init__(self):
        self.lista_todas_mesas = {}
        self.lista_reservadas= {} # Dicionário com as mesas ocupadas e por quais clientes

    def adicionar_mesa(self, mesa: Mesa):
        """"
        adicionar_mesa(self, mesa: Mesa)
            -> Adiciona uma mesa ao restaurante.
        :param self: Referente a instância.
        :param mesa:Mesa: Recebe um objeto da class Mesa, atribuindo um número a mesma.
            -> Receberá o número da Mesa adicionada, criando um dicionário com a ID dela, colocado no mesa:Mesa
        """
        self.lista_todas_mesas[mesa.numero] = mesa

    def verificar_disponibilidade(self, quantia_pessoas):
        """"
        verificar_disponibilidade(self, quantia_pessoas):
            -> Verifica quais mesas estão disponíveis para o número de pessoas passado como parametro.
        :param quantia_pessoas: Número de pessoas para a reserva, se passar pelos filtros de disponibilidade, mostra ao terminal ID da mesa.
            -> Se nenhuma mesa estiver disponível, informa no terminal.
        """
        disponivel = []
        for key, mesa in self.lista_todas_mesas.items():
            if mesa.disponivel:
                if mesa.capacidade >= quantia_pessoas:
                    disponivel.append(mesa)
        if len(disponivel) == 0:
            print(f'Sem mesas disponíveis para {quantia_pessoas} pessoas.')
        elif len(disponivel) > 0:
            print('Mesa Disponivel -> ', end ='')
            for c in disponivel:
                print(f'Mesa: ID {c.numero} - ', end = '')
        return disponivel

    def reservar(self, numero_reserva, pessoa: Cliente):
        """
        reservar(self, numero_reserva, pessoa: Cliente):
            -> Recebe o número da mesma que quer reservar e atribui ao objeto de Class Cliente.
        :param numero_reserva: ID da mesa que deseja reservar, deve checar as disponíveis antes.
        :param pessoa: Recebe objeto da Class Cliente, atribuindo ele ao ID da mesa que quer reservar.
        :return: Se tiver como reservar, return True.
        """
        for keys, mesa in self.lista_todas_mesas.items():
            if keys == numero_reserva:
                if mesa.disponivel:
                    if mesa.capacidade >= pessoa.num_pessoas:
                        mesa.disponivel = False
                        self.lista_reservadas[numero_reserva] = pessoa
                        print(f'Reserva confirmada! Mesa {numero_reserva} para {pessoa.nome}!')
                        return True


    def cancelar_reserva(self, idmesa):
        """"
        cancelar_reserva(self, idmesa):
            -> Recebe o ID da mesa reservada e cancela, tornando ela disponível novamente.
        :param idmesa: ID da mesa que deseja cancelar reserva.
        """
        if idmesa in self.lista_reservadas.keys():
            self.lista_reservadas.pop(idmesa)
            for keys, mesa in self.lista_todas_mesas.items():
                if idmesa == keys:
                    if not mesa.disponivel:
                        mesa.disponivel = True

    def verificar_reservadas(self):
        """"
        verificar_reservadas(self)
            -> Sem parametro, mostra lista das mesas já reservadas e quem reservou.
        """
        for mesa_reservada, cliente_reservou in self.lista_reservadas.items():
            print(f'A mesa {mesa_reservada} foi reservada por {cliente_reservou.nome}')

cliente1 = Cliente('Wally', 1, 6)
cliente2 = Cliente('Gabriel',2, 10 )
mesa1 = Mesa(1, 6)
mesa2 = Mesa(2, 12)
restaurante = Restaurante()
restaurante.adicionar_mesa(mesa1)
restaurante.adicionar_mesa(mesa2)
restaurante.reservar(1, cliente1)
restaurante.cancelar_reserva(2)
restaurante.verificar_disponibilidade(5)

