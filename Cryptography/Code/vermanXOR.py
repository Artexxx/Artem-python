"""
(Шифр Вернама является шифром с абсолютной криптостойкостью, т.к. использует случайные ключи для каждого символа.
В данном примере шифр Вернама основан на XOR шифровании

      Message: rip and tear until
          Key: None
Final message: ('13.97.97.118.53.100.103.104.52.120.102.102.114.10.112.126.108.107.103', '7.19.8.6.21.5.9.12.20.12.3.7.0.0.5.16.24.2.11')
"""

from random import randint
from re import findall


def regular(text):
    return findall(r"[0-9]+", text)


def encryptDecrypt(mode, message, final=[], keys=[]):
    if mode == 'E':
        for symbol in message:
            key = randint(0, 25)
            keys.append(str(key))
            final.append(str(ord(symbol) ^ key))
        return '.'.join(final), '.'.join(keys)
    else:
        keys = input("Write the keys: ")
        for index, symbol in enumerate(regular(message)):
            final.append(chr(int(symbol) ^ int(regular(keys)[index])))
        return ''.join(final)


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not found")
        raise SystemExit
    startMessage = input("Write the message: ")
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
