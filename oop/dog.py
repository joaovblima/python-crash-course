class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} esta agora sentado.")
    
    def roll_over(self):
        print(f"{self.name} rolou.")


my_dog = Dog("Mel", 2)
print(f"o nome do meu cachorro eh: {my_dog.name}")
print(f"a idade do meu cachorr eh {my_dog.age}")
my_dog.roll_over()
my_dog.sit()

your_dog = Dog("fred", 10)
print(f"o nome do meu cachorro eh {your_dog.name}")
print(f"a idade eh {your_dog.age}")
your_dog.sit()