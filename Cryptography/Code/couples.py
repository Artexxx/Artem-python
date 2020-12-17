"""
Шифр пар -- является шифром замены. Есть привязка между двумя символами.
Eсли в тексте попадается символ A, он заменяется на B (A → B), но это также действует и в обратную сторону (B → A).)

      Message: rip and tear until
          Key: None
Final message:  QJO BMC SFBQ VMSJK
"""

KEYS = {
    'A': 'B', 'C': 'D', 'E': 'F', 'G': 'H', 'I': 'J', 'K': 'L',
    'M': 'N', 'O': 'P', 'Q': 'R', 'S': 'T', 'U': 'V', 'W': 'X',
    'Y': 'Z'}

message = list(input("Write the message: ").upper())

for symbol in range(len(message)):
    for key in KEYS:
        if message[symbol] == key:
            message[symbol] = KEYS[key]
        elif message[symbol] == KEYS[key]:
            message[symbol] = key

print("Final message:", "".join(message))
