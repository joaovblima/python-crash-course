prompt = "\nDigite algo que eu repetirei pra voce: "
prompt += "\nDigite 'quit' para encerrar o programa. "

ativo = True
mensagem = ""
while ativo:
    mensagem= input(prompt)
    if mensagem == "quit":
        ativo = False
    else:
        print(mensagem)
