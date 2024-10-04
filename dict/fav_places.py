favorite_places = {
    "joao": ["sitio", "ct", "casa", "igreja"],
    "ingrid": ["academia", "casa", "trabalho"],
    "maria": ["rua", "escola", "casa"]
}


for pessoas, lugares in favorite_places.items():
    print(f"{pessoas.title()}:")
    for lugar in lugares:
        print(f"{lugar}")
    print()

