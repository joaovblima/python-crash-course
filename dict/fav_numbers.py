numbers = {
    "joao": [9, 99],
    "lele": [10, 11],
    "ingrid": [15, 12222], 
    "touro": [19], 
    "lidiane": [33],
}

for nome, numeros in numbers.items():
    print(f"{nome.title()}")
    for numero in numeros:
        print(numero)
    print()