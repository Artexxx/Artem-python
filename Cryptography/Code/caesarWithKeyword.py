"""  Шифр Цезаря с ключевым словом -- обычный шифр Цезаря.
     метод шифрования меняет порядок символов в алфавите за счёт ключевого слова
"""
from string import ascii_uppercase

symbolsAlpha = list(ascii_uppercase)

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not Found!")
    raise SystemExit
rawStartMessage = input("Write the message: ").upper()
numberKey = int(input("Write the number key: "))
stringKey = list(input("Write the string key: ").upper())

startMessage = "".join([w for w in rawStartMessage if w.isalpha()])

def remove(alpha, raw_string):
    # clear string
    clear_string = "".join(s for s in raw_string if raw_string.count(s) > 1)

    for symbol in clear_string:
        if symbol in alpha:
            alpha.remove(symbol)

    return alpha, clear_string


def insert(alpha_string):
    for index, symbol in enumerate(alpha_string[1]):
        alpha_string[0].insert(index, symbol)
    return alpha_string[0]


def replace(alpha, key):
    while key > 0:
        alpha.insert(0, alpha[-1])
        del alpha[-1]
        key -= 1
    return alpha


def encryptDecrypt(mode, message, key, final=""):
    alphaS = symbolsAlpha[::]
    alphaC = replace(insert(remove(symbolsAlpha, stringKey)), key)
    print(alphaC)
    for symbol in message:
        if mode == 'E':
            final += alphaC[alphaS.index(symbol)]
        else:
            final += alphaS[alphaC.index(symbol)]
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage, numberKey))
