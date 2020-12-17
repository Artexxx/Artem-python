"""
Тарабарская грамота -- своего рода шифр пар.
Отличие заключено в замене только согласных символов.

      Message: rip and tear until
          Key: None
Final message: JIL AMW GEAJ UMGIP
"""
KEYS = {
    'B': 'Z', 'C': 'X', 'D': 'W', 'F': 'V', 'G': 'T',
    'H': 'S', 'J': 'R', 'K': 'Q', 'L': 'P', 'M': 'N'}
message = list(input("Write the text: ").upper())

for symbol in range(len(message)):
    for key in KEYS:
        if message[symbol] == key:
            message[symbol] = KEYS[key]
        elif message[symbol] == KEYS[key]:
            message[symbol] = key

print("Final message:", "".join(message))
