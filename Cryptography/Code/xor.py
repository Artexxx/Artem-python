"""
XOR шифрование основано на логической операции Исключающее ИЛИ.
Данное шифрование не требует переключателя.
      Message: rip and tear until
          Key: 13
Final message: d}-lci-yhl-xcyda
"""
# 1010, 0101 == 1111
# 1111, 0101 == 1010
message = list(input("Write the message: "))
key = input("Write the int key: ")
for symbol in range(len(message)):
    try:
        message[symbol] = chr(ord(message[symbol]) ^ int(key))
    except ValueError:
        message[symbol] = chr(ord(message[symbol]) ^ ord(key))
print("Final message:", "".join(message))

