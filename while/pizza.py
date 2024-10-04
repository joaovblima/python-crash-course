prompt= "\nDigite a cobertura que você deseja em sua pizza: "
prompt += "\n(Digite 'quit' para sair.) "

ativo = True

while ativo:
    cobertura = input(prompt)
    if cobertura == "quit":
        ativo = False
    else:
        print(f"Adicionando a cobertura sabor {cobertura.title()} na pizza.")