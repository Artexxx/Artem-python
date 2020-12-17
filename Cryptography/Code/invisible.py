"""
Невидимый шифр сочетает в себе элементы криптографии и стеганографии
Метод шифрования основан на конструкции шифра Бэкона, вместо символа A находится символ пробела, а вместо символа B - символ табуляции.

      Message: rip and tear until
          Key: None
Final message:
"""
from re import findall

dictKeys = {
    'A': '     ', 'N': ' \t\t \t',
    'B': '    \t', 'O': ' \t\t\t ',
    'C': '   \t ', 'P': ' \t\t\t\t',
    'D': '   \t\t', 'Q': '\t    ',
    'E': '  \t  ', 'R': '\t   \t',
    'F': '  \t \t', 'S': '\t  \t ',
    'G': '  \t\t ', 'T': '\t  \t\t',
    'H': '  \t\t\t', 'U': '\t \t  ',
    'I': ' \t   ', 'V': '\t \t \t',
    'J': ' \t  \t', 'W': '\t \t\t ',
    'K': ' \t \t ', 'X': '\t \t\t\t',
    'L': ' \t \t\t', 'Y': '\t\t   ',
    'M': ' \t\t  ', 'Z': '\t\t  \t',
}


def regular(text):
    template = r"[\t ]{5}"
    return findall(template, text)


def encryptDecrypt(mode, file, final=""):
    if mode == 'E':
        with open(file, 'w') as f:
            for symbol in input("Write the message: ").upper():
                if symbol in dictKeys:
                    final += dictKeys[symbol]
            print(final)
            f.write(final)
        return "File successfully saved"
    else:
        with open(file, 'r') as f:
            for cipher in regular(f.read()):
                for key in dictKeys:
                    if cipher == dictKeys[key]:
                        final += key
        return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    fileName = input("Write the fileName: ")
    print("Final message:", encryptDecrypt(cryptMode, fileName))
