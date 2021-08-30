# EXERCISE 9-15: LOTTERY ANALYSIS

from random import randint, choice

pool = list(range(1, 11)) + ["f", "j", "t", "z", "q"]

winner = str(choice(pool)) + str(choice(pool)) + str(choice(pool)) + \
            str(choice(pool))

print(f"Winning combination is: {winner}")

n = 0
while True:
    ticket = str(choice(pool)) + str(choice(pool)) + str(choice(pool)) + \
            str(choice(pool))
    n = n + 1
    if ticket == winner:
        print(f"Took {n} iterations to find a winner.")
        break
