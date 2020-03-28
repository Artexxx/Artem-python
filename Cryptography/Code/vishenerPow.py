""" Многоалфавитные шифры обладают способностью множественного шифрования,
    то-есть способны шифровать одно и то же сообщение многократно усиливая
    криптостойкость зашифрованного сообщения.)"""

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not Found!")
    raise SystemExit
startMessage = input("Write the message: ").upper()
numberKeys = int(input("How much keys: "))

listKeys = []
for index in range(numberKeys):
    listKeys.append(input(f"Write the keyWord[{index}]:").upper())


def encryptDecrypt(mode, message, keys, final=""):
    for key in keys:
        key *= len(message) // len(key) + 1
        for index, symbol in enumerate(message):
            if mode == 'E':
                temp = ord(symbol) + ord(key[index])
            else:
                temp = ord(symbol) - ord(key[index])
            final += chr(temp % 26 + ord('A'))
        message = final
        print(message)
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage, listKeys))
