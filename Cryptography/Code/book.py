""" Книжный шифр --  один из самых криптостойких методов шифрования.
    Особенность шифра заключена в ключе-книге, которым может являться любой
        текстовой информацией."""
from random import choice
from re import findall

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not Found!");
    raise SystemExit
startMessage = input("Write the message: ")
bookKey = input("Write the name file book-key: ")


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
                pass
    else:
        for numbers in regular(message):
            for indexKey, symbolKey in enumerate(book):
                if numbers == str(indexKey):
                    final += symbolKey
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage, bookKey))
