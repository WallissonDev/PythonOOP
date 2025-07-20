# Exercício sobre Polimorfismo - Proposto por IA

class Animal:

    def __init__(self):
        print('This is animal.')

    def scream(self):
        print('The animal made a sound.')

class Dog(Animal):

    def scream(self):
        print('Au Au Au!')

class Cat(Animal):

    def scream(self):
        print('Meow! Meow!')


cat_animal = Cat()
cat_animal.scream()