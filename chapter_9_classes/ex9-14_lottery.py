# EXERCISE 9-14: LOTTERY
from random import randint, choice

pool = list(range(1, 11)) + ["f", "j", "t", "z", "q"]

print(
    f"Any ticket that matches: {choice(pool)}{choice(pool)}{choice(pool)}"
    f"{choice(pool)} wins a prize."
)

