# shifr цезаря
# chr() - Функция преобразующая число в символ по ASCII таблице
# ord() - Функция преобразующая символ в число по ASCII таблице

cryptMode = input("[E]encrypt [D]decrypted\n[E or D]").upper()

if cryptMode not in ["D", "E"]:
    print("Error -> input E or D")
    raise SystemExit  # вызов исключения

startMassage = input("Write text ->").upper()

# если ключ не является числом – выводится ошибка
try:
    assKey = int(input("Write assKey ->"))
except ValueError:
    print("Error,key != INT")
    raise SystemExit


def encrypt_decrypt(mode, massage, key, final=""):
    """Основная функция принимающая аргументы: переключатель, сообщение, ключ"""
    for sumvol in massage:
        if mode == "E":  # Шифрование сообщения при помощи таблицы ASCII
            final += chr(ord(sumvol) + key)
        else:  # Decrypteed сообщения при помощи таблицы ASCII
            final += chr(ord(sumvol) - key)
    return final


print("Your final message:", encrypt_decrypt(cryptMode, startMassage, assKey))
