"""
Шифр замены – один из самых распространённых методов шифрования. В
    отличии от шифра Цезаря не имеет конкретного ключа и алгоритма шифрования.)

Message: rip and tear until
    Key: !@#$%^&*()-=+?:;<>/[]{}|.,~
Final message: >(;!?$[%!>]?[(=
"""
from string import ascii_uppercase

symbolsAlpha = ascii_uppercase
symbolsCrypt = (
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
    '=', '+', '?', ':', ';', '<', '>', '/', '[', ']', '{', '}', '|',
    '.', ',', '~')
KEYS = dict(zip(symbolsAlpha, symbolsCrypt))


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


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not found")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
