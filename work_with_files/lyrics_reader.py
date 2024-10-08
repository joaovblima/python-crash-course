from pathlib import Path
path = Path(input("Digite o caminho do arquivo: "))
contents = path.read_text()
print(contents)
for line in contents.splitlines():
    print(f"->{line}")