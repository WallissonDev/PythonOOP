from random import randint
from time import sleep

def cor(tom):
    cores = { 'limpa': '\033[m',
             'azul': '\033[34m',
             'amarelo': '\033[1;33m',
             'roxo': '\033[1;30;45m',
             'vermelho': '\033[30;41m',
             'pretoebranco': '\033[7;30m',
              'cinza': '\033[7;40m'
             }
    return cores[tom]

class CSBox:

    def __init__(self):
        self.dicionario = \
              {f'{cor('cinza')}G3SG1 - Desert Storm{cor('limpa')}': [40001, 80000],
              f'{cor('cinza')}Nova - Sand Dune{cor('limpa')}': [1, 40000],
              f'{cor('cinza')}SCAR-20 - {cor('limpa')}': [89031, 92040],
              f'{cor('cinza')}MP5-SD - Necro Jr.{cor('limpa')}': [86021, 89030],
              f'{cor('cinza')}PP-Bizon - Runic{cor('limpa')}' : [83011,  92784],
              f'{cor('cinza')}Galil AR - Cold Fusion{cor('limpa')}': [92785, 93528],
              f'{cor('cinza')}Five-Seven - Coolant{cor('limpa')}': [80001, 83010],
              f'{cor('cinza')}P90 - Freight{cor('limpa')}':[99811, 99910],
              f'{cor('cinza')}SG 553 - Aloha{cor('limpa')}': [99961, 99510],
              f'{cor('cinza')}Glock-18 - Weasel{cor('limpa')}':[99975, 99934],
              f'{cor('cinza')}Five-Seven - Violent Daimyo{cor('limpa')}': [99981, 99922],
              f'{cor('roxo')}Glock-18 - Water Elemental{cor('limpa')}': [99989, 99984],
              f'{cor('roxo')}M4A1-S - Leaded Glass{cor('limpa')}': [99987, 99986],
              f'{cor('roxo')}AK-47 - Point Disarray{cor('limpa')}': [99993, 99994],
              f'{cor('vermelho')}M4A1-S - Hyper Beast{cor('limpa')}': [99995, 99995],
              f'{cor('vermelho')}M4A1-S - Cyrex{cor('limpa')}':[99996, 99997],
              f'{cor('vermelho')}AWP - Hyper Beast{cor('limpa')}': [99998, 99998],
              f'{cor('vermelho')}AK-47 - Aquamarine Revenge{cor('limpa')}': [99999, 100000]
              }
        self.inventario = []
    
    def menu(self):
        print(f'{cor('amarelo')}='*30)
        print(f'Bem-Vindo ao FreeLootBox do Fox'.center(30))
        print('='*30)
        print('0 - Verificar Skins Disponíveis')
        print('1 - Verificar Chance de Skins Disponíveis')
        print('2 - Abrir 1 Caixa')
        print('3 - Abrir quantia personalizada')
        print('4 - Abrir até Drop Lendário')
        print('5 - Verificar Inventário')
        print(f'6 - Fechar Tigrinho{cor('limpa')}')

    def abrir_menu(self):
        while True:
            self.menu()
            esc = int(input('Opção: '))
            sleep(1)
            if esc == 0:
                self.itens()
            if esc == 1:
                pass
            if esc == 2:
                self.abrir_caixa()
            if esc == 3:
                quantia = int(input('Quantas: '))
                self.abrir_varias(quantia)
            if esc == 4:
                self.abrir_lendario()
            if esc == 5:
                for c in self.inventario:
                    print(c)
            if esc == 6:
                break
    
    def abrir_caixa(self):
        girando = randint(1, 100000)
        for item, chance in self.dicionario.items():
            if girando >= chance[0] and girando <= chance[1]:
                print(f'Você dropou: {item}')
                self.inventario.append(item)
                (sleep(2))
                return self.inventario

    def abrir_varias(self, quantidade):
        dropadas = []
        while len(dropadas) != quantidade:
            girando = randint(1, 93528)
            for item, chance in self.dicionario.items():
                if girando >= chance[0] and girando <= chance[1]:
                    dropadas.append(item)
                    self.inventario.append(item)
                    break
        print('Itens Dropados: ')
        for c in dropadas:
            print(f'{c}')
        return self.inventario

    def abrir_lendario(self):
        dias = anos = 0
        while True:
            girando = randint(1, 100000)
            if girando >= 99995 and girando <= 100000:
                for item, chance in self.dicionario.items():
                    if chance[0] >= girando and chance[1] <= girando:
                        print(f'Você encontrou um lendário: {item} Levaram {dias} dias -> {anos} anos.')
                        self.inventario.append(item)
                        return self.inventario
            else:
                dias += 1
                if dias % 365 == 0:
                    anos += 1

    def itens(self):
        for itens, chance in self.dicionario.items():
            print(f'Item: {itens} - Chance: {chance}')
