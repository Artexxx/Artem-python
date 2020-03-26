""" Шифр Атбаш --Создаёт зеркальную версию алфавита,
                где начало - буква ’Z’, а конец алфавита буква - ‘A’.)"""

message = input("Write the message: ").upper()

alphaDefault = [chr(x) for x in range(65, 91)]
alphaReverse = alphaDefault[::-1]

final = ""
for symbolMessage in message:
    for indexAlpha, symbolAlpha in enumerate(alphaDefault):
        if symbolMessage == symbolAlpha:
            final += alphaReverse[indexAlpha]
print("Final message:", final)
