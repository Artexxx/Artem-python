""" Шифр Бэкона -- шифр замены, который можно представить в виде
        двоичного кода, где A = 0, B = 1. Особенность шифра Бэкона заключается в
        гибкости использования, что позволяет применять его в различных методах
        стеганографии"""
from re import findall

keysBacon = {
    'A': "AAAAA", 'B': "AAAAB", 'C': "AAABA",
    'D': "AAABB", 'E': "AABAA", 'F': "AABAB",
    'G': "AABBA", 'H': "AABBB", 'I': "ABAAA",
    'J': "ABAAB", 'K': "ABABA", 'L': "ABABB",
    'M': "ABBAA", 'N': "ABBAB", 'O': "ABBBA",
    'P': "ABBBB", 'Q': "BAAAA", 'R': "BAAAB",
    'S': "BAABA", 'T': "BAABB", 'U': "BABAA",
    'V': "BABAB", 'W': "BABBA", 'X': "BABBB",
    'Y': "BBAAA", 'Z': "BBAAB", ' ': "BBABA"
}
cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode is not Found!");
    raise SystemExit
startMessage = input("Write the message: ").upper()


def regular(text):
    """ Делит сообщение по 5 символов и отбрасывает лишние"""
    template = r"[A-Z]{5}"
    return findall(template, text)


def encryptDecrypt(mode, message, final=""):
    if mode == 'E':
        for symbol in message:
            if symbol in keysBacon: final += keysBacon[symbol]
    else:
        print(regular(message))
        for symbolsFive in regular(message):
            for key in keysBacon:
                if symbolsFive == keysBacon[key]: final += key
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage))

