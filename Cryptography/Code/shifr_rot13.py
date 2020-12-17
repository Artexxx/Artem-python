"""
Шифр ROT13 – часть шифра Цезаря с позицией 13.
Особенность ROT13 заключена в принципе инволюции, при которой не нужен переключатель режимов шифрования/расшифрования

      Message: rip and tear until
          Key: None
Final message: EVCGNAQGGRNEGHAGVY
"""

message = list(input("WRITE THE MASSAGE ->").upper())
for sumvol in range(len(message)):
    message[sumvol] = chr(ord(message[sumvol]) % 26 + ord("A"))

print("Your final message:", "".join(message))

