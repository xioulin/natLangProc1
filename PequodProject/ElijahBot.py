from chatterbot import Chatbot

chatbot= Chatbot('Chatpot')

exit_conditions= (';q','quit','exit')

print("what be your name?")
name = input()
print(f"Ay, ur name be {name}")

while True:
    query = input('>')
    if query in exit_conditions:
        break
    else:
        print(f'{chatbot.get_response(query)}')






