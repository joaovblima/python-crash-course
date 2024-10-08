print("me forneca dois numeros e eu farei a divisao.")
print("digite q para sair")

while True:
    first_number = input("Primeiro numero: ")
    if first_number == "q":
        break
    second_number = input("segundo numero: ")
    if second_number == "q":
        break


    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("voce nao pode dividir por zero.")
    else:
        print(answer)