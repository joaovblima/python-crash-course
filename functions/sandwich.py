def make_sandwich(*ingredients):
    print("Hm, lets make your sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"-> {ingredient}")

make_sandwich("calabresa")
make_sandwich("queijo", "presunto")
make_sandwich("2 hamburguers", "salada", "salsicha", "bacon")