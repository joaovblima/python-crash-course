#contando ate 20
for i in range(1, 21):
    print(i)

print()
numeros = [i for i in range(1, 1000001)]
for numero in numeros:
    print(numero)
print("MEnor numero: ")
print(min(numeros))
print("Maior numero: ")
print(max(numeros))
print("Soma: ")
print(sum(numeros))
print("Numeros impares de 1 a 20")
for i in range(1, 20, 2):
    print(i)
print("Multiplos de 3 ate 30: ")
lista_multiplo_tres = [i for i in range(3, 30, 3)]
for num in lista_multiplo_tres:
    print(num)
print("Cubos: ")
for i in range(1, 10):
    print(i **3)
lista_de_cubos = [i**3 for i in range(1, 11)]


