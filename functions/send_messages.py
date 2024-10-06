messages = ["sao paulo é o maior do Brasil", "jiujitsu é bom demais", "deus é bom demais"]
recived_messages = []

def send_messages(list_messages, sent_messages):
    print("...preparing for shipping...")
    for message in list_messages:
        print(f"MENSAGEM ENVIADA: {message.title()}")
        
    while list_messages:
        add_message = list_messages.pop()
        sent_messages.append(add_message)
    



send_messages(list_messages=messages, sent_messages=recived_messages)
print(messages)
print(recived_messages)