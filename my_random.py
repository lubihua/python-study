from random import randint


class Die:

    def __init__(self):
        self.sides = randint(1, 30)

    def show_sides(self):
        print('random number is ' + str(self.sides))


Die().show_sides()
Die().show_sides()
Die().show_sides()
