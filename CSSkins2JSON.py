from random import randint
from time import sleep
import json

with open('itemscs.json', 'r', encoding='utf-8') as armas:
    kit = json.load(armas)

class CSBox:

    def __init__(self, armas):
        self.dicionario = armas
        self.inventario = []

    def menu(self):
        print(f'=' * 30)
        print(f'Bem-Vindo ao FreeLootBox do Fox'.center(30))
        print('=' * 30)
        print('0 - Verificar Skins Disponíveis')
        print('1 - Verificar Chance de Skins Disponíveis')
        print('2 - Abrir 1 Caixa')
        print('3 - Abrir quantia personalizada')
        print('4 - Abrir até Drop Lendário')
        print('5 - Verificar Inventário')
        print(f'6 - Fechar Tigrinho')

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
        menor = min(self.dicionario.values())
        maior = max(self.dicionario.values())
        girando = randint(menor[0], maior[1])
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
        menor = min(self.dicionario.values())
        maior = max(self.dicionario.values())
        while True:
            girando = randint(menor[0], maior[1])
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

objeto = CSBox(kit)
objeto.abrir_menu()