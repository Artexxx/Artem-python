"""
Шифр Тритемиуса – улучшенный шифр Цезаря в котором ключём является не число, а какая-либо функция.
В отличии от шифра Цезаря не подвержен частотному криптоанализу, т.к. шифрует сообщение по индексам

      Message: rip and tear until
          Key: None
Final message: RKTGVNFSQJOJRIN
"""


def encryptDecrypt(mode, message, key, final=""):
    for index, symbol in enumerate(message):
        if mode == 'E':
            temp = ord(symbol) + key(index) - 13
        else:
            temp = ord(symbol) - key(index) - 13
        final += chr(temp % 26 + ord('A'))
    return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit

    rawMessage = list(input("Write the message: ").upper())
    startMessage = [i for i in rawMessage if i.isalpha()]

    funcKey = lambda x: x * 2

    print("Final message:", encryptDecrypt(cryptMode, startMessage, funcKey))
