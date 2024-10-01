foods = ["arroz", "macarrão", "feijão", "carne moída", "salada", "purê de batata"]
print("Os três primeiros itens da lista são: ")
for food in foods[:3]:
    print(food)
print("Os três itens do meio da lista são: ")
for food in foods[2:5]:
    print(food)

print("Os três ultimos itens da lista são: ")
for food in foods[3:]:
    print(food)