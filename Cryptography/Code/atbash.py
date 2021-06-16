"""
Шифр Атбаш -- cоздаётся зеркальная версия алфавита, где начало - буква ’Z’, а конец алфавита буква - ‘A’.

      Message: rip and tear until
          Key: None
Final message: IRKZMWGVZIFMGRO
"""

from string import ascii_uppercase

message = input("Write the message: ").upper()

alphaDefault = ascii_uppercase
alphaReverse = alphaDefault.

final = ""
for symbolMessage in message:
    for indexAlpha, symbolAlpha in enumerate(alphaDefault):
        if symbolMessage == symbolAlpha:
            final += alphaReverse[indexAlpha]
print("Final message:", final)
