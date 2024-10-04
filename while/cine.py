prompt ="\nDigite a idade do visitate: "

valor_a_pagar = 0

idade = int(input(prompt))
if idade < 3:
    print("Ingresso gratuito.")
elif idade > 3 and idade < 12:
    print("Seu ingresso custará R$ 10,00")
else:
    print("Seu ingresso custará R$ 15,00")