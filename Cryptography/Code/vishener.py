"""
Шифр Виженера -- самый знаменитый многоалфавитный шифр.
Построен на конструкции шифра Цезаря. Представлен в виде квадрата и
содержит в себе фактически 26 шифров Цезаря с разными смещениями по алфавиту

      Message: rip and tear until
          Key: doom guy
Final message: UWDFTTXRWSODMAHRLZ
"""


def encryptDecrypt(mode, message, key, final=""):
    key *= len(message) // len(key) + 1
    for index, symbol in enumerate(message):
        if mode == 'E':
            temp = ord(symbol) + ord(key[index])
        else:
            temp = ord(symbol) - ord(key[index])
        final += chr(temp % 26 + ord('A'))
    return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    oneKey = input("Write the key: ").upper()
    print("Final message:", encryptDecrypt(cryptMode, startMessage, oneKey))
