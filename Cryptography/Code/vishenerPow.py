"""
Многоалфавитные шифры обладают способностью множественного шифрования,
то-есть способны шифровать одно и то же сообщение многократно усиливая
криптостойкость зашифрованного сообщения.

      Message: rip and tear until
         Keys: {doom guy, doom marine}
Final message: XKRRMFXIEFSGAOTKXZ
"""


def encryptDecrypt(mode, message, keys, final=""):
    for key in keys:
        final = ""
        key *= len(message) // len(key) + 1
        for index, symbol in enumerate(message):
            if mode == 'E':
                temp = ord(symbol) + ord(key[index])
            else:
                temp = ord(symbol) - ord(key[index])
            final += chr(temp % 26 + ord('A'))
        message = final
    return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    numberKeys = int(input("How much keys: "))

    listKeys = []
    for index in range(numberKeys):
        listKeys.append(input(f"Write the keyWord[{index}]:").upper())

    print("Final message:", encryptDecrypt(cryptMode, startMessage, listKeys))
