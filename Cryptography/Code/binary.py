"""
Двоичный код — это способ представления данных в виде кода, в котором каждый разряд принимает одно из двух возможных значений, обычно обозначаемых цифрами 0 и 1.

      Message: rip and tear until
          Key: None
Final message: 01110010 01101001 01110000 00100000 01100001 01101110 01100100 00100000 01110100 01100101 01100001 01110010 00100000 01110101 01101110 01110100 01101001 01101100
"""


def encodeDecode(mode, message, final=""):
    if mode == 'E':
        for symbol in message:
            final += "{0:08b} ".format(ord(symbol))
    else:
        for code in message.split():
            final += chr(int(code, 2))
    return final


if __name__ == '__main__':
    codeMode = input("[E]ncode|[D]ecode: ").upper()
    if codeMode not in ['E', 'D']:
        print("Error: mode is not Found!")
        raise SystemExit
    startMessage = input("Write the message: ")
    print("Final message:", encodeDecode(codeMode, startMessage))
