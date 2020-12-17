"""
Индексированный шифр
метод шифрования создаёт ключ, который будет являться последовательностью символов открытого сообщения без повторений.

      Message: rip and tear until
          Key: None
Final message: ('rip andteul', '0 1 2 3 4 5 6 3 7 8 4 0 3 9 5 7 1 10')
"""
from re import findall


def regular(text):
    return findall(r"[0-9]+", text)


def encryptDecrypt(mode, message, final="", key=""):
    if mode == 'E':
        for x in message: key += x if x not in key else ""
        encrypt = {key[x]: str(x) for x in range(len(key))}
        for symbol in message:
            final += encrypt[symbol] + ' '
        return (key, final)
    else:
        key = input("Write the key: ")
        for num in regular(message):
            final += key[int(num)]
        return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ")
    print("Final message: ", encryptDecrypt(cryptMode, startMessage))
