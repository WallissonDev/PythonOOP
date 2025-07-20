class Human:
    def __init__(self, name):
       self.name = name

    def creation(self, create = []):
        create.append(self.name)

class Man(Human):

    def __init__(self, name, gender):
        Human.__init__(self, name)
        self.gender = gender

class Woman(Human):

    def __init__(self, name, gender):
       Human.__init__(self, name)
       self.gender = gender

God = Human('God')
Adam = Man('Adam', 'Man')
Eve = Woman('Eve','Woman')
print(God.creation(Adam,Eve))

# According to the creation myths of the Abrahamic religions,
# Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job.
# The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman.
# Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.