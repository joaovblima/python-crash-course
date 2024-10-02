current_users = ["joao", "mathesus", "lele", "lidiane", "ingrid"]
new_users = ["joao", "ingrid", "maria sofia", "maria alice"]

for user in new_users:
    if user in current_users:
        print(f"{user} precisará escolher outro nome de usuario")
    else:
        print(f"o nome {user} está disponivel ")