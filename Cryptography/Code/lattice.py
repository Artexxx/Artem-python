"""
Шифр решётки скрывает открытое сообщение в ложных символах.

      Message: rip and tear until
          Key: None
   Final keys: [6, 12, 22, 23, 25, 37, 38, 55, 56, 60, 63, 64, 66, 79, 80, 84, 91, 94]
Final message:
        0   1   2   3   4   5   6   7   8   9
    0 | m | a | w | s | H | C | r | k | f | j |
    1 | l | t | i | t | s | k | d | U | Y | t |
    2 | B | r | p |   | D | a | U | J | Z | D |
    3 | y | T | w | X | N | R | f | n | d | E |
    4 | W | T | z | H | i | r | j | k | K | A |
    5 | l | y | F | n | X |   | t | V | u | w |
    6 | e | V | c | a | r | i |   | m | N | O |
    7 | K | D | W | l | I | M | N | D | p | u |
    8 | n | F | P | G | t | e | q | k | w | r |
    9 | I | i | X | M | l | B | t | W | m | Q |
"""

from random import choice, randint
from string import ascii_letters

squade = 10

alphaList = ascii_letters
stringList = [choice(alphaList) for _ in range(squade * squade)]


def getKey(text):
    while True:
        keys = [randint(0, 99) for _ in range(len(text))]
        for number in keys:
            switch = False
            if keys.count(number) > 1:
                switch = True
                break
        if switch == False:
            return keys


def lattice(index=0):
    print(end='    ')
    for string in range(squade):
        print(string, end='   ')
    for string in range(squade):
        print()
        for column in range(squade):
            if index % squade == 0:
                print(index // squade, end=' | ')
            print(stringList[index], end=' | ')
            index += 1
    print()


if __name__ == '__main__':
    message = input("Write the message: ")
    keyList = getKey(message)

    keyList.sort()
    print("Keys:", keyList)

    for index, symbol in enumerate(message):
        del stringList[keyList[index]]
        stringList.insert(keyList[index], symbol)
    lattice()
