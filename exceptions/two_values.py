soma = 0
while True:
    entrada = input("Digite numeros para somar. Aperta 'q' para sair. ")

    if entrada == "q":
        break
    try:
        numero = int(entrada)
    except ValueError:
        print("Voce precisa digitar um numero para somar.")
    else:
        soma += numero
print(soma)