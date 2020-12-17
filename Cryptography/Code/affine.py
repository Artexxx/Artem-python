"""
Аффинный шифр основан на шифре Цезаря.
Особенность метода шифрования заключена в модульной арифметике.

      Message: rip and tear until
          Key: {11 15}
Final message: UZYQPCWQQHPUQBCQZG
"""


def encryptDecrypt(mode, message, key, final=""):
    for symbol in message:
        if mode == 'E':
            # (a * s + b) mod 26
            final += chr((int(key[0]) * ord(symbol) + int(key[1]) - 13) % 26 + ord('A'))
        else:
            # A^2(y + 26 - b) mod 26
            final += chr(pow(int(key[0]), 11) * ((ord(symbol) + 26 - int(key[1]) - 13)) % 26 + ord('A'))
    return final


if __name__ == '__main__':
    print("Possible Key[a]: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.")
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    numberKeys = input("Write the int keys: ").split()
    if len(numberKeys) != 2:
        print("Error: qualitity keys must be 2")
        raise SystemExit
    print("Final message:", encryptDecrypt(cryptMode, startMessage, numberKeys))
