"""
Шифр Хилла основан на линейной алгебре и модульной арифметике.

MatrixKey = |9 49|
            |2 11|
[#] опредилитель матрицы 9*11 - 49*2 (!должен быть == 1)

      Message: rip and tear until
          Key: [[9, 49], [2, 11]]
Final message: ZSNNDEBFLBRW
"""

from re import findall
from string import ascii_uppercase

matrixLength = 2
MatrixKey = [[9, 49], [2, 11]]
det = MatrixKey[0][0] * MatrixKey[1][1] - MatrixKey[0][1] * MatrixKey[1][0]
if det != 1:
    print("Error: determinant != 1")
    raise SystemExit

# Создание обратной матрицы.
iMatrixKey = [
    [MatrixKey[1][1], -MatrixKey[0][1]],
    [-MatrixKey[1][0], MatrixKey[0][0]]]

ALPHA = ascii_uppercase


def regular(text):
    template = r"[A-Z]{2}"
    return findall(template, text)


"""
пример кодирования букв `HE` в `ZG`
`HE` = |9 49| * |7 `H`| -> |9*7 + 49*4| -> |259mod 26| -> `Z`
       |2 11|   |4 `E`|    |2*7 + 11*4|    |58 mod 26| -> `G`

пример декодирования букв `ZG` в `HE` 
`ZG` = |11 -49| * |25 `Z`| -> |11*25 + -49*6| -> |-19 mod 26| -> `H`
       |-2  9 |   |6  `G`|    |-2*25 +   9*6|    |  4 mod 26| -> `E`
"""


def encryptDecrypt(message, matrix, summ=0, final=""):
    for double in range(len(message)):
        for string in range(matrixLength):
            for column in range(matrixLength):
                summ += matrix[string][column] * ALPHA.index(message[double][column])
            final += ALPHA[(summ) % 26]
            summ = 0
    return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ").upper()

    while len(startMessage) % matrixLength != 0: startMessage += 'Z'
    if cryptMode == 'E':
        finalMessage = encryptDecrypt(regular(startMessage), MatrixKey)
    else:
        finalMessage = encryptDecrypt(regular(startMessage), iMatrixKey)
    print("Final message:", finalMessage)
