class Privileges:

    def __init__(self, privileges=["pode adicionar post", "pode deletar post", "pode banir usuario"]):
        self.privileges = privileges
    
    def show_privileges(self):
        print("Admin pode: ")
        for privilege in self.privileges:
            print(f"-> {privilege.title()}")
        