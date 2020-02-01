"""Шифр ROT13 – часть шифра Цезаря с позицией 13. Особенность ROT13
заключена в принципе инволюции, при которой не нужен переключатель режимов
шифрования/расшифрования"""

massage = list(input("WRITE THE MASSAGE ->").upper())
for sumvol in range(len(massage)):
    massage[sumvol] = chr(ord(massage[sumvol]) % 26 + ord("A"))  # Шифрование сообщения при помощи таблицы ASCII.

print("FINAL MESSAGE:".join(massage))
