"""
Ложные символы используются для увеличения криптостойкости шифра.
Могут быть использованы во множестве методов шифрования.

      Message: rip and tear until
          Key: None
Final message: ?)< !-$} [%!"? ]-\[')_
"""

from random import randint, choice
from string import ascii_uppercase

traps = ('"', '\\', '{', '}', '`', '№', '\'')
symbolAlpha = ascii_uppercase
symbolCrypt = ('!', '@', '#', '$', '%', '^', '&', '*', ')', '(', '~',
               '_', '+', '-', '=', '<', '>', '?', '/', '[', ']', ',', '|', ':', ';', '.')
keys = dict(zip(symbolAlpha, symbolCrypt))


def encryptDecrypt(mode, message, final=""):
    if mode == 'E':
        length = len(message) // 4
        for _ in range(length):
            message.insert(randint(0, len(message)), choice(traps))
        for symbol in message:
            if symbol in keys:
                final += keys[symbol]
            else:
                final += symbol
    else:
        for symbol in message:
            for key in keys:
                if symbol == keys[key]:
                    final += key
    return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit

    startMessage = list(input("Write the message: ").upper())
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
