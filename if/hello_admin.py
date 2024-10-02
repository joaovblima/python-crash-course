users = ["joao", "mathesus", "lele", "lidiane", "admin"]

if users:
    for user in users:
        if user == "admin":
            print("Olá admin, você gostaria de ver o relatório?")
        else:
            print(f"Ola {user}, obrigado por fazer login novamente")
else:
    print("Precisamos adicionar alguns usuarios.")