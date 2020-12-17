"""
Псевдосимвольный шифр -- основан на шифре Бэкона.
Особенность шифрования заключена в 3х одинаковых внешне символах, но различающихся в кодировке Unicode.
Один символ ’A’ взят из латиницы, другой из кириллицы, третий из греческого алфавита.

      Message: rip and tear until
          Key: None
Final message: АΑΑAΑΑАΑAΑΑΑAAAАААAАAΑΑΑΑAАAААAAAАΑΑΑΑΑΑAΑАААΑAАAΑΑАAΑ
"""
from re import findall

keysPsevdo = {
    'A': "AAA", 'B': "AAА", 'C': "AAΑ",
    'D': "AАA", 'E': "AАА", 'F': "AАΑ",
    'G': "AΑA", 'H': "AΑА", 'I': "AΑΑ",
    'J': "АAA", 'K': "АAА", 'L': "АAΑ",
    'M': "ААA", 'N': "ААА", 'O': "ААΑ",
    'P': "АΑA", 'Q': "АΑА", 'R': "АΑΑ",
    'S': "ΑAA", 'T': "ΑAА", 'U': "ΑAΑ",
    'V': "ΑАA", 'W': "ΑАА", 'X': "ΑАΑ",
    'Y': "ΑΑA", 'Z': "ΑΑА", ' ': "ΑΑΑ"
}


def regular(text):
    return findall(r"\w{3}", text)


def encryptDecrypt(mode, message, final=""):
    if mode == 'E':
        for symbol in message:
            if symbol in keysPsevdo:
                final += keysPsevdo[symbol]
    else:
        for threeSymbols in regular(message):
            for key in keysPsevdo:
                if threeSymbols == keysPsevdo[key]:
                    final += key
    return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not found")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
