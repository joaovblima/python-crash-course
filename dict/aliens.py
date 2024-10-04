"""
alien_0 = {"cor": "preto",
           "pontos": 14}
alien_1 = {"cor": "branco",
           "pontos": 10}
alien_2 = {"cor": "rosa",
           "pontos": 2}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
"""


aliens_2 = []

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens_2.append(new_alien)


for alien in aliens_2[:3]:
    if alien["color"] == "green":
        alien["color"] ="yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
print("...")

for alien in aliens_2[:5]:
    print(alien)

print(f"quantos aliens foram criados: {len(aliens_2)}")