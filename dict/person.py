joao = {
    "first_name": "joao", 
    "last_name": "lima", 
    "age": 27,
    "city": "uniao dos palmares", 
}

ingrid = {
    "first_name": "ingrid",
    "last_name": "melo",
    "age": 24,
    "city": "uniao dos palmares"
}

maria_sofia = {
    "first_name": "maria",
    "last_name": "sofia",
    "age": 6,
    "city": "uniao dos palmares"
}

people = [joao, ingrid, maria_sofia]


for person in people:
        full_name = f"{person["first_name"]} {person["last_name"]}"
        age = f"{person["age"]}"
        city = f"{person["city"]}"
        print(f"FULLNAME: {full_name}")
        print(f"idade: {age}")
        print(f"cidade: {city}\n")