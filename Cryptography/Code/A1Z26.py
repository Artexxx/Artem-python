""" Шифр A1Z26 является одним из самых лёгких методов шифрования.
    Принцип шифрования заключён в нумерации символа алфавита: A = 1, B = 2 … Z = 26."""

from re import findall
from string import ascii_uppercase

ALPHA = ascii_uppercase

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not found")
    raise SystemExit
startMessage = input("Write the message: ").upper()


def regular(text):
    return findall(r"[0-9]+", text)


def encryptDecrypt(mode, message, final=""):
    if mode == 'E':
        for symbol in message:
            final += "%hu " % (ALPHA.index(symbol) + 1)
    else:
        for number in regular(message):
            final += "%c" % ALPHA[int(number) - 1]
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage))
