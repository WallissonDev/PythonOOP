class Animal:

    def __init__(self, sound):
        self.sound = sound

    def action(self):
        print(f'The animal made a sound = {self.sound}')

class Dog(Animal):

    def __init__(self, sound, name):
        Animal.__init__(self, sound)
        self.name = name

    def action(self):
        Animal.action(self)

animal_dog = Animal('AwAw')
animal_dog.action()
another_dog = Dog('AwwwAwwww', 'Rex')
another_dog.action()




