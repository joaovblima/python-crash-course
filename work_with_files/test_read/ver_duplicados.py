from pathlib import Path
print("Bem vindo ao comparador de listas.")
lista1 = Path(input("Digite o caminho da sua primeira lista: "))
lista2 = Path(input("Digite o caminho da sua segunda lista: "))
ler_lista1 = lista1.read_text()
ler_lista2 = lista2.read_text()

for pessoa in ler_lista1.splitlines():
    if pessoa in ler_lista2:
        print(f"ATENÇÃO, DUPLICADO -> {pessoa}")