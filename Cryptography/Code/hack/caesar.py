"""  BruteForce шифра Цезаря.
     Всего существует 25 вариантов дешифровки шифра Цезаря"""

cryptMessage = input("Write the message: ").upper()
print("All possible variants of decrypt:")

for key in range(26):
    for symbol in cryptMessage:
        print(chr((ord(symbol) - key - 13) % 26 + ord('A')), end='')
    print("\t key =", key)
