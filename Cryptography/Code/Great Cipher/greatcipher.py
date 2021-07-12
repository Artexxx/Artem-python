"""
Великий Шифр собрал в себя 5 различных методов шифрования:
    омофоническое шифрование, кодирование, замена слогов, ложные символы,
    специальные символы (символы редактирования текста).
Шифр является одним из самых криптостойких.

      Message: rip and tear until
          Key: None
Final message: 096.058.206.288.232.252.023.009.225.197.161.328.247.114.255.098.238.175.212.035.166.255.076.007.330.188
"""

from memory import KEY, LIMIT
from random import randint, choice
from re import findall

# ________________________________________ Омофоническое шифрование
# Количество занимаемого места памяти: 118
keysCrypt = {
    'A': KEY[0:8], 'B': KEY[8:10],
    'C': KEY[10:13], 'D': KEY[13:17],
    'E': KEY[17:29], 'F': KEY[29:31],
    'G': KEY[31:33], 'H': KEY[33:39],
    'I': KEY[39:45], 'J': [KEY[45]],
    'K': [KEY[46]], 'L': KEY[47:51],
    'M': KEY[51:53], 'N': KEY[53:59],
    'O': KEY[59:66], 'P': KEY[66:68],
    'Q': [KEY[68]], 'R': KEY[69:75],
    'S': KEY[75:81], 'T': KEY[81:90],
    'U': KEY[90:93], 'V': [KEY[93]],
    'W': KEY[94:96], 'X': [KEY[96]],
    'Y': KEY[97:99], 'Z': [KEY[99]],
    ' ': KEY[100:118]
}
# ________________________________________ Кодирование
# Количество занимаемого места памяти: 137
listWord = ('TO', 'WHY', 'WITH', 'WAR', 'NOT', 'IN', 'OR', 'ELSE', 'THE', 'THAT', 'BY',
            'AND', 'HOW', 'BUT', 'IF', 'ONE', 'YOU', 'ME', 'USE', 'HIS', 'YOUR', 'ON', 'OF', 'WAS', 'BE',
            'THIS', 'WHAT', 'THEY', 'NO', 'YES', 'TRUE', 'FALSE', 'CALL', 'FEEL', 'CLOSE', 'VERY',
            'WHICH', 'CAR', 'ANY', 'HOLD', 'WORK', 'RUN', 'NEVER', 'START', 'EVEN', 'LIGHT', 'THAN',
            'AFTER', 'PUT', 'STOP', 'OLD', 'WATCH', 'FIRST', 'MAY', 'TALK', 'ANOTHER', 'BEHIND',
            'CUT', 'MEAN', 'SMILE', 'OUR', 'MUCH', 'IT', 'HE', 'SHE', 'ITS', 'HOUSE', 'KEEP', 'YEAH',
            'PLACE', 'BEGIN', 'NOTHING', 'YEAR', 'MAN', 'WOMAN', 'BECAUSE', 'THREE', 'SEEM', 'ARE',
            'WAIT', 'NEED', 'LAST', 'LATE', 'SURE', 'BIG', 'SMALL', 'FRONT', 'REALLY', 'NAME', 'ALL',
            'NEW', 'GUY', 'ANYTHING', 'SHOULD', 'KILL', 'POINT', 'WALL', 'BLACK', 'STEP', 'SECOND',
            'LIFE', 'MAYBE', 'FALL', 'OWN', 'FAR', 'WHILE', 'FOR', 'HELP', 'END', 'THOSE', 'SAME',
            'REACH', 'GIRL', 'STREET', 'NEXT', 'FEW', 'FEET', 'SHOW', 'MUST', 'TABLE', 'OK', 'IS',
            'OKAY', 'BODY', 'PHONE', 'ADD', 'WATER', 'FIRE', 'INSIDE', 'BREAK', 'EVER', 'SHAKE',
            'MEET', 'GREAT', 'MIND', 'ENOUGH', 'MINUTE', 'FOLLOW', 'ATTACK', 'DEAD', 'ALMOST')

position = 118  # 118
keysCode = {listWord[x]: KEY[x + position] for x in range(len(listWord))}

# _______________________________________ Замена слогов и символов
# Количество занимаемого места памяти: 46
listSyllables = ('TH', 'WH', 'EE', 'AI', 'OO', 'IS', 'ING', 'ED', 'BE', 'ON', 'OR', 'ER',
                 'CH', 'SH', 'GH', 'EN', 'EA', 'OU', 'LL', 'US', 'SE', 'AL', 'ST', 'EV', 'WO', 'UI', 'IN', 'RE',
                 '!', '?', '.', ',', '@', '#', '$', '%', '*', '^', '-', '+', '=', '/', ':', ';', '&', '~')

position = len(listWord) + 118  # 137 + 118 = 255
keysSyllables = {listSyllables[x]: KEY[x + position] for x in range(len(listSyllables))}

# _____________________________________ Специальные символы
# Количество занимаемого места памяти: 4
listSpecial = ('<-', '->', '<+', '+>')

position = len(listWord) + len(listSyllables) + 118  # 137 + 46 + 118 = 301
keysSpecial = {listSpecial[x]: KEY[x + position] for x in range(len(listSpecial))}

# _______________________________ Ложные символы
# 350 - (4 + 137 + 46 + 118) = 45
position = len(listWord) + len(listSyllables) + len(listSpecial) + 118

# Количество занимаемого места памяти: 45
traps = tuple([KEY[x] for x in range(position, LIMIT)])

# Удаление неиспользуемых элементов
del listWord, listSpecial, position

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not Found!")
    raise SystemExit
startMessage = input("Write the message: ").upper()


def regular(text):
    template = r"[0-9]{3}"
    return findall(template, text)


def encryptDecrypt(mode, message, final="", string=""):
    if mode == 'E':
        secondText = findall(r"[^\s]+", message)
        del message

        # Внедрение в код специальных символов
        for indexWord in range(len(secondText)):
            if secondText[indexWord] in keysSpecial:
                secondText[indexWord] = keysSpecial[secondText[indexWord]]

        # Кодирование слов на числа
        for indexWord in range(len(secondText)):
            if secondText[indexWord] in keysCode:
                secondText[indexWord] = keysCode[secondText[indexWord]]

        # Замена слогов на числа
        for indexWord in range(len(secondText)):
            for syllable in keysSyllables:
                if syllable in secondText[indexWord]:
                    secondText[indexWord] = secondText[indexWord].replace(syllable, keysSyllables[syllable])

        # Разделение всех слов на символы
        for indexWord in range(len(secondText)):
            secondText[indexWord] = list(secondText[indexWord])
        for indexWord in range(len(secondText)):
            secondText[indexWord].append(' ')

        # Шифрование всех символов на числа
        for indexWord in range(len(secondText)):
            for indexSymbol in range(len(secondText[indexWord])):
                symbol = secondText[indexWord][indexSymbol]
                if symbol in keysCrypt:
                    length = len(keysCrypt[symbol])
                    secondText[indexWord][indexSymbol] = keysCrypt[symbol][randint(0, length - 1)]

        # Соединение всех чисел в одну строку и разделение по три
        for word in secondText:
            string += "".join(word)
        finalList = list(regular(string))

        # Внедрение в код ложных символов
        for indexList in range(len(finalList)):
            randSwitch = randint(0, 2)
            randPosition = randint(0, len(finalList))
            if not randSwitch: finalList.insert(randPosition, choice(traps))

        for word in finalList:
            final += "".join(word)
        return ".".join(regular(final))

    else:
        for symbolText in regular(message):
            for element in keysSpecial:  # Перебор всех специальных символов
                if symbolText == keysSpecial[element]: final += element
            for word in keysCode:  # Перебор всех кодов
                if symbolText == keysCode[word]: final += word
            for syllable in keysSyllables:  # Перебор всех слогов
                if symbolText == keysSyllables[syllable]: final += syllable
            for symbol in keysCrypt:  # Перебор всех шифров
                if symbolText in keysCrypt[symbol]: final += symbol

        listWord = findall(r"[^\s]+", final)

        # Опции специальных символов
        for _ in range(len(listWord)):
            for element in keysSpecial:
                if element in listWord:
                    if element == '<-':
                        del listWord[listWord.index(element) - 1]
                        listWord.remove(element)
                    elif element == '->':
                        del listWord[listWord.index(element) + 1]
                        listWord.remove(element)
                    elif element == '<+':
                        listWord[listWord.index(element)] = listWord[listWord.index(element) - 1]
                    elif element == '+>':
                        listWord[listWord.index(element)] = listWord[listWord.index(element) + 1]
                    else:
                        pass
        final = " ".join(listWord)
        return final


finalMessage = encryptDecrypt(cryptMode, startMessage)
print("Final message:", finalMessage)
