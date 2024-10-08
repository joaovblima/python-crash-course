from pathlib import Path

path = Path("guest.txt")
name = input("Digite seu nome: ")
path.write_text(name)
