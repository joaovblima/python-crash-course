prompt = "\nSe você pudesse visitar um lugar no mundo, onde seria? "

ativo = True

respostas = {}
while ativo:
    nome = input("Qual seu nome? ")
    resposta = input(prompt)

    respostas[nome] = resposta

    opcao = input("Deseja que aluguem mais responda? (sim / nao) ")
    if opcao == "nao":
        ativo = False


for pessoa, resposta in respostas.items():
    print(f"{pessoa.title()} gostaria de viajar para {resposta}")
    
    
    
