class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} ta eleito.")
    
    def greeting(self):
        print(f"BOm dia {self.first_name}")
    
    def increment_login_attempts(self, number_of_attempts):
        self.login_attempts += number_of_attempts
        print(f"O numero de tentativas de login foi atualizado: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attemps = 0
        print("...O numero de tentativas de login foi resetado...")





    