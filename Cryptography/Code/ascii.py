"""
ASCII — название таблицы (кодировки, набора), в которой некоторым распространённым печатным и непечатным символам сопоставлены числовые коды.

      Message: rip and tear until
          Key: None
Final message: 114 105 112 32 97 110 100 32 116 101 97 114 32 117 110 116 105 108
"""

def encodeDecode(mode, message, final=""):
    if mode == 'E':
        for symbol in message:
            final += str(ord(symbol)) + ' '
    else:
        for code in message.split():
            final += chr(int(code))
    return final


if __name__ == '__main__':
    codeMode = input("[E]ncode|[D]ecode: ").upper()
    if codeMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ")
    print("Final message:", encodeDecode(codeMode, startMessage))
