# EXERCISE 9-13: DICE

from random import randint, choice

class Die:
    """Class that can represent an any-sided die."""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(f"You've rolled a {roll}")

d6 = Die(6)
d10 = Die(10)
d20 = Die(20)

for rolls in range(1, 11):
    d6.roll_die()

for rolls in range(1, 11):
    d10.roll_die()

for rolls in range(1, 11):
    d20.roll_die()

