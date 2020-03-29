""" Шифр Штакетник относится к шифрам перестановки и является одним из самых
    лёгких в своём роде.
    Принцип шифрования – разделение всех символов на чётные и нечётные позиции,
    а далее совмещение групп символов, сначала чётные, потом нечётные.)"""

cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E', 'D']:
    print("Error: mode not in (E/D)")
    raise SystemExit
startMessage = input("Write the message: ").upper()


def encryptDecrypt(mode, message, final=""):
    if mode == 'E':
        final += message[::2] + message[1::2]
    else:
        if len(message) % 2 != 0: message += ' '
        half = len(message) // 2
        evenLetters = message[:half]
        oddLetters = message[half:]
        for index in range(half):
            final += evenLetters[index] + oddLetters[index]
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage))
