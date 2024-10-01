pizzas = ["calabresa", "frango com catupiry", "file com queijo do reino", "nordestina"]
friends_pizzas = pizzas[:]
pizzas.append("marguerita")
friends_pizzas.append("banana flambada")
print("minhas pizzas favoritas: ")
for pizza in pizzas:
    print(pizza)
print()
print("pizzas dos meus amigos: ")
for pizza in friends_pizzas:
    print(pizza)
