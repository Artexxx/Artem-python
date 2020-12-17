"""
Кодирование – шифр замены. замена целых слов на какой-либо шифртекст/слово.

      Message: rip and tear until
          Key: None
Final message: RIP ! TEAR UNTIL
"""

WORDS = ('AND', 'THE', 'OR', 'ALL', 'ANY', 'WHAT', 'WHY', 'YES', 'NO',
         'ONE', 'YOU', 'HE', 'SHE', 'USE', 'IF', 'ELSE', 'THIS', 'THAN', 'YOUR',
         'ON', 'HOW', 'ARE', 'ME', 'IT', 'IS', 'THAT', 'WAS', 'OF', 'BE', 'OK')
CODES = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
         '+', '=', '/', '?', '<', '>', ';', ':', '{', '}', '[', ']', '~', ',', '.', '"', '|', '\\')
KEYS = dict(zip(WORDS, CODES))


def encryptDecrypt(mode, message):
    for key in KEYS:
        if mode == 'E':
            if key in message:
                message = message.replace(key, KEYS[key])
        else:
            if KEYS[key] in message:
                message = message.replace(KEYS[key], key)
    return message


if __name__ == '__main__':
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E', 'D']:
        print("Error: mode is not found")
        raise SystemExit
    startMessage = input("Write the message: ").upper()
    print("Final message:", encryptDecrypt(cryptMode, startMessage))
