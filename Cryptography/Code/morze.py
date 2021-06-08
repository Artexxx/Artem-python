"""
Азбука Морзе предназначена для передачи инфы по телеграфу.
    тире  - длинный сигнал
    точка - короткий

    Message: rip and tear until
          Key: None
Final message: .-. .. .--. .- -. -.. - . .- .-. ..- -. - .. .-..
"""
CODES = {
    'A': '.-', 'N': '-.', '1': '.----',
    'B': '-...', 'O': '---', '2': '..---',
    'C': '-.-.', 'P': '.--.', '3': '...--',
    'D': '-..', 'Q': '--.-', '4': '....-',
    'E': '.', 'R': '.-.', '5': '.....',
    'F': '..-.', 'S': '...', '6': '-....',
    'G': '--.', 'T': '-', '7': '--...',
    'H': '....', 'U': '..-', '8': '---..',
    'I': '..', 'V': '...-', '9': '----.',
    'J': '.---', 'W': '.--', '0': '-----',
    'K': '-.-', 'X': '-..-',
    'L': '.-..', 'Y': '-.--',
    'M': '--', 'Z': '--..',
}


def encodeDecode(mode, message, final=""):
    if mode == 'E':
        for symbol in message:
            if symbol not in CODES:
                message = message.replace(symbol, '')
        for symbol in message:
            final += CODES[symbol] + ' '
    else:
        for code in message.split():
            for symbol in CODES:
                if code == CODES[symbol]:
                    final += symbol
    return final


if __name__ == '__main__':
    codeMode = input("[E]ncode|[D]ecode: ").upper()
    if codeMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit(0)
    startMessage = input("Write the message: ").upper()
    print("Final message:", encodeDecode(codeMode, startMessage))
