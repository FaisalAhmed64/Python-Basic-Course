import random

for i in range(10):
    print(random.randint(1, 30))

memebrs = ["mosh", "faisal", "rasel", "rudel"]
print(random.choices(memebrs))


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
