class Ship:

    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        self.crew = self.crew * 1.5
        loot = self.draft - self.crew
        if loot > 20:
            return True
        else:
            return False

Titanic = Ship(40,3)
print(Titanic.is_worth_it())

##Every time your spies see a new ship enter the dock, they will create a new ship object
#based on their observations:
#draft - an estimate of the ship's weight based on how low it is in the water
#crew - a count of the crew onboard
#Taking into account that each crew member onboard adds 1.5 to the draft,
#the ships that would otherwise have a draft of more than 20 are considered worthy to board.
#Any ship weighing that much must have a lot of booty!