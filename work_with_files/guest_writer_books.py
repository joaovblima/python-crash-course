from pathlib import Path
path = Path("guest_books.txt")

activate = True
livros = []
print("Digite o nome dos seus livros favoritos.\n")
print("Aperte 'q' a qualquer momento para sair.")
while activate:
    livro = input("Nome do livro: ")
    if livro == "q":
        activate = False
    else:
        livros.append(livro)


path.write_text("\n".join(livros) + "\n", encoding="utf-8")