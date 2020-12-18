"""
Двойная цифирь -- шифр перестановки по определённому ключу.
Принцип шифрования – разделение текста на две части в виде таблицы образуя тем самым пары символов.
Далее пары символов индексируются и переставляются местами. В итоге индексы будут являться ключами

      Message: rip and tear until
          Key: None
Final message: RPADTA NII N ERUTL
    Final key: 1.3.5.7.2.0.6.4.8

"""

from re import findall
from random import choice


def regular(text):
    template = r"[0-9]+"
    return findall(template, text)


def encryptDecrypt(mode, message, final='', key=[]):
    if mode == 'E':
        if len(message) % 2 != 0: message.append(' ')
        listHalf = [
            message[len(message) // 2:],
            message[:len(message) // 2]]
        # keys {0: [ C  A ], 1: [ B  D ], 2: [ S  F ]}
        keys = {x: [listHalf[0][x], listHalf[1][x]] for x in range(len(message) // 2)}
        listKey = [x for x in range(len(keys))]
        print(listKey, keys)
        newList = []
        # newList [[ S  F ], [ C  A ], [ B  D ]]
        for _ in range(len(keys)):
            choiceKey = choice(listKey)
            key.append(str(choiceKey))
            newList.append(keys[choiceKey])
            listKey.remove(choiceKey)
        print(newList)
        for listIndex in range(len(newList)):
            for symbol in newList[listIndex]:
                final += symbol
        return final, '.'.join(key)
    else:
        listHalf = [
            [message[x] for x in range(len(message)) if x % 2 != 0],
            [message[y] for y in range(len(message)) if y % 2 == 0]]
        key = regular(input("Write the key: "))
        key = [int(x) for x in key]
        keys = {y: [listHalf[0][x], listHalf[1][x]] for x, y in enumerate(key)}
        finalList = [
            [keys[x][0] for x in range(len(keys)) if x in keys],
            [keys[y][1] for y in range(len(keys)) if y in keys]]
        for i in range(2):
            for index in range(len(message) // 2):
                final += finalList[i][index]
        return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = list(input("Write the message: ").upper())
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
