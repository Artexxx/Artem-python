# Affine Cipher Hacker
import detectEnglish
from string import ascii_letters

SILENT_MODE = False
SYMBOLS = ascii_letters


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def decryptMessage(message, key, final=""):
    for symbol in message:
        # A^2(y + 26 - b) mod 26
        final += chr(pow(int(key[0]), 11) * ((ord(symbol) + 26 - int(key[1]) - 13)) % 26 + ord('A'))
    return final


def hackAffine(message):
    print('Hacking...')
    # Brute-force by looping through every possible key
    for key in range(len(SYMBOLS) ** 2):
        keyA = getKeyParts(key)[0]
        if gcd(keyA, len(SYMBOLS)) != 1:
            continue
        decryptedText = decryptMessage(message, [keyA, key])
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


myMessage = """OWBZIV"""
hackedMessage = hackAffine(myMessage)
if hackedMessage != None:
    print(hackedMessage)
else:
    print('Failed to hack encryption.')
