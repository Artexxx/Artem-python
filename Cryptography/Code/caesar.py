"""
Шифр Цезаря -- один из самых простых и наиболее широко известных методов шифрования.

      Message: rip and tear until
          Key: 3
Final message: ULSWDQGWWHDUWXQWLO
"""


def encrypt_decrypt(mode, massage, key, final=""):
    for symbol in massage:
        if mode == "E":
            final += chr((ord(symbol) + key - 13) % 26 + ord("A"))
        else:
            final += chr((ord(symbol) - key - 13) % 26 + ord("A"))
    return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    startKey = int(input("Write the int keys: "))
    print("Your final message:", encrypt_decrypt(cryptMode, startMessage, startKey))
