""" Роторное шифрование построено на принципе шифра Вернама, то-есть с каждым
    новым поступающим на вход символом ключ будет изменяться по роторам,
    имитуруя случайность. """
from string import ascii_uppercase

ROTORS = (
    (10, 24, 14, 12, 23, 2, 7, 15, 24, 2, 7, 5, 22, 6, 2, 1, 22, 12, 6, 9, 7, 2, 11, 23, 14, 2),
    (1, 7, 11, 26, 12, 5, 11, 20, 11, 7, 18, 6, 17, 18, 19, 1, 13, 5, 2, 9, 11, 13, 6, 17, 26, 24),
    (9, 1, 21, 6, 4, 19, 25, 6, 17, 10, 26, 1, 23, 6, 1, 17, 19, 17, 25, 21, 3, 21, 17, 1, 18, 20)
)

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not Found!")
    raise SystemExit
startMessage = input("Write the message: ").upper()


def encryptDecrypt(mode, message, final=""):
    x, y, z = 1, 2, 3
    for symbol in message:
        rotor = ROTORS[0][x] + ROTORS[1][y] + ROTORS[2][z]
        if mode == 'E':
            if symbol in ascii_uppercase:
                final += chr((ord(symbol) - 13 + rotor) % 26 + ord('A'))
            else:
                continue
        else:
            final += chr((ord(symbol) - 13 - rotor) % 26 + ord('A'))

        if x != 25:
            x += 1
        else:
            x = 0
            if y != 25:
                y += 1
            else:
                y = 0
                if z != 25:
                    z += 1
                else:
                    z = 0
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage))
