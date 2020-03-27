""" Шифр Атбаш --Создаёт зеркальную версию алфавита,
                где начало - буква ’Z’, а конец алфавита буква - ‘A’.)"""

from string import ascii_uppercase

message = input("Write the message: ").upper()

alphaDefault = ascii_uppercase
alphaReverse = alphaDefault[::-1]

final = ""
for symbolMessage in message:
    for indexAlpha, symbolAlpha in enumerate(alphaDefault):
        if symbolMessage == symbolAlpha:
            final += alphaReverse[indexAlpha]
print("Final message:", final)
