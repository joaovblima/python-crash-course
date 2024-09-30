print("#1")
name = "Joao Lima"
personal_message = f"Ola {name}, você gostaria de aprender um pouco de Python hoje?"
print(personal_message)
print()

print("#2")
print(name.title())
print(name.upper())
print(name.lower())

print()
print("#3")
print('Olavo de Carvalho certa vez disse: "Há coisas que são boas por alguns instantes, outras por algum tempo. Só algumas são para sempre."')

print()
print("#4")
famous_person = "Olavo de Carvalho"
message = "Há coisas que são boas por alguns instantes, outras por algum tempo. Só algumas são para sempre."
full_message = f"{famous_person} certa vez disse: {message}"
print(full_message)

print()
print("#5")
trash_name = "    \tLord\n Voldemort"
print(trash_name)
print(trash_name.lstrip())
print(trash_name.rstrip())
print(trash_name.strip())

print()
print("#6")
filename = "python_notes.txt"
print(filename)
filename = filename.removesuffix(".txt")
print(filename)