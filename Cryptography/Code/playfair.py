"""
Шифр Плейфера является биграммным шифром.
Особенность шифра заключена в матрице 5x5 в которой мы заменяем символы нашего сообщения.
Принцип шифрования – если два символа находятся на одной строке матрицы, значит
    сместить индексы этих двух символов на одну позицию вперёд в этой же строке.
Если символы находятся на разных строках, значит прочертить прямоугольник и
    заменить символы на другие края прямоугольника

      Message: rip and tear until
          Key: MATRIX
Final message: GPIUDNSTUGAQAOVQD
"""

from string import ascii_uppercase
from re import findall

MATRIX = [
    ['S', 'O', 'M', 'E', 'T'],
    ['H', 'I', 'N', 'G', 'A'],
    ['B', 'C', 'D', 'F', 'K'],
    ['L', 'P', 'Q', 'R', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]
addSymbol = 'X'


def regular(text):
    template = r"[A-Z]{2}"
    return findall(template, text)


def encryptDecrypt(mode, message, final=""):
    if mode == 'E':
        for symbol in message:
            if symbol not in ascii_uppercase:
                message.remove(symbol)
        for index in range(len(message)):
            if message[index] == 'J': message[index] = 'I'
        for index in range(1, len(message)):
            if message[index] == message[index - 1]:
                message.insert(index, addSymbol)
        if len(message) % 2 != 0:
            message.append(addSymbol)

    binaryList = regular("".join(message))
    for binary in range(len(binaryList)):
        binaryList[binary] = list(binaryList[binary])
        for indexString in range(len(MATRIX)):
            for indexSymbol in range(len(MATRIX[indexString])):
                if binaryList[binary][0] == MATRIX[indexString][indexSymbol]:
                    y0, x0 = indexString, indexSymbol
                if binaryList[binary][1] == MATRIX[indexString][indexSymbol]:
                    y1, x1 = indexString, indexSymbol
        for indexString in range(len(MATRIX)):
            if MATRIX[y0][x0] in MATRIX[indexString] and MATRIX[y1][x1] in MATRIX[indexString]:
                if mode == 'E':
                    x0 = x0 + 1 if x0 != 4 else 0
                    x1 = x1 + 1 if x1 != 4 else 0
                else:
                    x0 = x0 - 1 if x0 != 0 else 4
                    x1 = x1 - 1 if x1 != 0 else 4
        y0, y1 = y1, y0
        binaryList[binary][0] = MATRIX[y0][x0]
        binaryList[binary][1] = MATRIX[y1][x1]
    for binary in range(len(binaryList)):
        for symbol in binaryList[binary]:
            final += symbol
    return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = list(input("Write the message: ").upper())
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
