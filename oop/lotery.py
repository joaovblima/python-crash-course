"""
from random import choices

sorteio = [10, 23, 43, 9, 5, 12, 39, 84, 3, "g", "i", "f", "x", "l"]
bilhete = []

for i in range(4):
    i = choices(sorteio)
    bilhete.append(i)
print("Eis o bilhete vencedor: ")
for opc in bilhete:
    print(opc, end="")
"""

from random import sample

sorteio = [10, 23, 43, 9, 5, 12, 39, 84, 3, "g", "i", "f", "x", "l"]
bilhete = sample(sorteio, 4)

print("O bilhete premiado é:",''.join(map(str, bilhete)) )