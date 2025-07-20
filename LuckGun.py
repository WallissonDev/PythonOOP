class BoxOpen:

    def GoldenItemChance(self):
        from random import randint
        years = days =  0
        while True:
            roll = randint(1,999999)
            if roll >= 999993:
                print(f'Item = {roll}')
                return print(f'Took -> Years: {years} Days: {days}'), roll
            else:
                days += 1
                if days % 365 == 0:
                    years += 1


Test = BoxOpen()
Test.GoldenItemChance()