from random import randint
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dices(self):
        num = randint(1, self.sides)
        print(num)

dez_lados = Dice(10)
dez_lados.roll_dices()
dez_lados.roll_dices()
dez_lados.roll_dices()
dez_lados.roll_dices()
dez_lados.roll_dices()
dez_lados.roll_dices()
dez_lados.roll_dices()
dez_lados.roll_dices()
dez_lados.roll_dices()
dez_lados.roll_dices()
print("-")
vinte_lados = Dice(20)
vinte_lados.roll_dices()
vinte_lados.roll_dices()
vinte_lados.roll_dices()
vinte_lados.roll_dices()
vinte_lados.roll_dices()
vinte_lados.roll_dices()
vinte_lados.roll_dices()
vinte_lados.roll_dices()
vinte_lados.roll_dices()
vinte_lados.roll_dices()