prompt = "\nPor favor digite o nome de uma cidade que voce ja visitou:"
prompt += "\n(Digite 'quit' quando terminar.) "


while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"Eu adoraria visitar {city.title()}")