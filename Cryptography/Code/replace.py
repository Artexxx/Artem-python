"""Шифр замены – один из самых распространённых методов шифрования. В
    отличии от шифра Цезаря не имеет конкретного ключа и алгоритма шифрования.)"""
from string import ascii_uppercase

symbolsAlpha = ascii_uppercase
symbolsCrypt = (
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
    '=', '+', '?', ':', ';', '<', '>', '/', '[', ']', '{', '}', '|',
    '.', ',', '~')
KEYS = dict(zip(symbolsAlpha, symbolsCrypt))

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not found")
    raise SystemExit

startMessage = input("Write the message: ").upper()


def encryptDecrypt(mode, message, final=""):
    if mode == 'E':
        for symbol in message:
            if symbol in KEYS:
                final += KEYS[symbol]
    else:
        for symbol in message:
            for key in KEYS:
                if symbol == KEYS[key]:
                    final += key
    return final

print("Final message:", encryptDecrypt(cryptMode, startMessage))
