""" Шифровальная машина <Typex> основана на роторном шифровании и шифре пар.
    Фактически является шифровальной машиной <Enigma> с убранным
    изъяном, который заключался в инволюции (рефлекторах). Именно поэтому
    <Typex> требует переключателя режимов шифрования"""

from string import ascii_uppercase

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not Found!")
    raise SystemExit
startMessage = input("Write the message: ").upper()

ROTORS = (
    (10, 24, 14, 12, 23, 2, 7, 15, 24, 2, 7, 5, 22, 6, 2, 1, 22, 12, 6, 9, 7, 2, 11, 23, 14, 2),
    (1, 7, 11, 26, 12, 5, 11, 20, 11, 7, 18, 6, 17, 18, 19, 1, 13, 5, 2, 9, 11, 13, 6, 17, 26, 24),
    (9, 1, 21, 6, 4, 19, 25, 6, 17, 10, 26, 1, 23, 6, 1, 17, 19, 17, 25, 21, 3, 21, 17, 1, 18, 20)
)
SWITCH = {
    'H': 'Z', 'S': 'N', 'L': 'M',
    'P': 'Q', 'R': 'W', 'X': 'Y'
}


def stageOne(message):
    message = list(message)
    for symbol in range(len(message)):
        for key in SWITCH:
            if message[symbol] == key:
                message[symbol] = SWITCH[key]
            elif message[symbol] == SWITCH[key]:
                message[symbol] = key
    return "".join(message)


def stageTwo(mode, message, final=""):
    X, Y, Z = 2, 0, 1  # Позиция роторов
    x, y, z = 1, 2, 3  # Ключевая настройка
    for symbol in message:
        rotor = ROTORS[X][x] + ROTORS[Y][y] + ROTORS[Z][z]
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


def encryptDecrypt(mode, message):
    if mode == 'E':
        message = stageOne(message)
        message = stageTwo(mode, message)
    else:
        message = stageTwo(mode, message)
        message = stageOne(message)
    return message


print("Final message:", encryptDecrypt(cryptMode, startMessage))
