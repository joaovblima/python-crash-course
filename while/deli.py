sandwich_orders = ["x-tudo","pastrami", "x-salada", "pastrami", "x-frango", "smash", "minuano", "pastrami"]
finished_orders = []

print("Infelizmente a lanchonete ficou sem pastrami")
while sandwich_orders:
    order = sandwich_orders.pop()
    if order == "pastrami":
        continue
    print(f"Eu fiz um {order}")
   
    finished_orders.append(order)

print(f"Todos os sanduiches que foram preparados:")
for finished_order in finished_orders:
    print(finished_order)