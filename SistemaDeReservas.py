class Cliente:

    def __init__(self, nome, identificador, num_pessoas):
        self.nome = nome
        self.identificador =  identificador
        self.num_pessoas = num_pessoas

class Mesa:

    def __init__(self, numero, capacidade, disponivel = True):
        self.numero = numero
        self.capacidade = capacidade
        self.disponivel = disponivel

class Restaurante:

    def __init__(self):
        self.lista_mesasdisp = [] # Lista de Mesas Disponíveis
        self.lista_reservadas= {} # Dicionário com as mesas ocupadas e por quais clientes
        self.lista_amostragem = [] # Apenas para mostrar ao terminal quais clientes e mesas estão interligados

    def disponiveis(self, objeto: Mesa):
        if objeto.disponivel:
            self.lista_mesasdisp.append(objeto)

    def verificar_disponibilidade(self):
        for mesas in self.lista_mesasdisp:
            if mesas.disponivel:
                print(f'Mesas Disponíveis {mesas.numero} - Capaciadade: {mesas.capacidade}')

    def reservar(self, numero_reserva, pessoa: Cliente):
        for mesas in self.lista_mesasdisp:
            if mesas.numero == numero_reserva:
                if pessoa.num_pessoas <= mesas.capacidade:
                    self.lista_reservadas['MesaID'] = mesas.numero
                    self.lista_reservadas['Cliente'] = pessoa.nome
                    self.lista_reservadas['ClienteID'] = pessoa.identificador
                    self.lista_reservadas['Pessoas'] = pessoa.num_pessoas
                    self.lista_amostragem.append(self.lista_reservadas.copy())
                    mesas.disponivel = False
        return False

    def cancelar_reserva(self, numero_reserva):
        for mesas in self.lista_amostragem:
            if numero_reserva == mesas['MesaID']:
                self.lista_amostragem.remove(mesas)
                # CORRIGIR ESSE MÉTODO
        for mesas in self.lista_mesasdisp:
            if mesas.numero == numero_reserva:
                mesas.disponivel = True

    def verificar_reservadas(self):
        for reservadas in self.lista_amostragem:
            print(reservadas)

cliente1 = Cliente('Matheus',1, 13)
cliente2 = Cliente('Maria', 2, 13)
cliente3 = Cliente('Joana', 3, 18)
cliente4 = Cliente('Diego', 4, 15)
mesa1 = Mesa(1, 6)
mesa2 = Mesa(2, 6)
mesa3 = Mesa(3, 12)
mesa4 = Mesa(4, 12)
restaurante = Restaurante()
restaurante.disponiveis(mesa1)
restaurante.disponiveis(mesa2)
restaurante.disponiveis(mesa3)
restaurante.disponiveis(mesa4)
restaurante.reservar(2, cliente2)
restaurante.reservar(3, cliente4)
restaurante.cancelar_reserva(2)
restaurante.verificar_reservadas()
restaurante.cancelar_reserva(3)
