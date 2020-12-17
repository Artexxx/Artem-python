"""
Шифр порты -- биграммный метод шифрования.
Смысл в шифровании двух символов триадой чисел.
Чаще всего представляется в виде таблицы, где по горизонтали и вертикали символы алфавита, а в самой таблице находятся триады чисел

      Message: rip and tear until
          Key: None
Final message: 451.014.499.018.534.503
"""

from string import ascii_uppercase
from re import findall

stageOne = ['00' + str(x) for x in range(1, 10)]
stageTwo = ['0' + str(x) for x in range(10, 100)]
stageThree = [str(x) for x in range(100, 677)]

N = tuple(stageOne + stageTwo + stageThree)

del stageOne, stageTwo, stageThree

coordinateX = ascii_uppercase
coordinateY = ascii_uppercase

cryptKeys = {x: None for x in N}
keys = tuple([key for key in cryptKeys])

# cryptKey = { 001: AA, 002 : AB ... 676: ZZ }
counter = 0
for x in coordinateX:
    for y in coordinateY:
        cryptKeys[keys[counter]] = x + y
        counter += 1

del N, coordinateX, coordinateY, counter, keys


def regular(mode, text):
    if mode == 'E':
        template = r"[A-Z]{2}"
    else:
        template = r"[0-9]{3}"
    return findall(template, text)


def encryptDecrypt(mode, message, final=[]):
    if mode == 'E':
        if len(message) % 2 != 0: message += 'Z'
        for symbols in regular(mode, message):
            for key in cryptKeys:
                if symbols == cryptKeys[key]:
                    final.append(key)
    else:
        for number in regular(mode, message):
            if number in cryptKeys:
                final.append(cryptKeys[number])
    return ".".join(final)


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode not in (E/D)")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
