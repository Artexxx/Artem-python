"""
Книжный шифр --  один из самых криптостойких методов шифрования.
Особенность шифра заключена в ключе-книге, которым может являться любой текстовой информацией.

      Message: rip and tear until
          Key: book.txt
Final message: 1955/850/33/1077/1851/1943/2508/185/1005/963/1946/2514/2493/13/20/2257/158/537/44/62/1173/1675/2446/2208/1941/936/2385/1888/1167/
"""
from random import choice
from re import findall


def regular(text):
    template = r"[0-9]+"
    return findall(template, text)


def encryptDecrypt(mode, message, key, final=""):
    with open(key) as bookKey:
        book = bookKey.read()
    if mode == 'E':
        for symbolMessage in message:
            listIndexKey = []
            for indexKey, symbolKey in enumerate(book):
                if symbolMessage == symbolKey:
                    listIndexKey.append(indexKey)
            try:
                final += str(choice(listIndexKey)) + '/'
            except IndexError:
                print(f"\x1b[0;30;41m [#] Symbol `{symbolMessage}` is not in the {key}! \x1b[0m")
    else:
        for numbers in regular(message):
            for indexKey, symbolKey in enumerate(book):
                if numbers == str(indexKey):
                    print(numbers, symbolKey)
                    final += symbolKey
    return final


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ")
    bookKey = input("Write the name file book-key: ")
    print("Final message:", encryptDecrypt(cryptMode, startMessage, bookKey))

