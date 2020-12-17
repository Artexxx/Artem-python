"""
Криптографические хеш-функции не предназначены для расшифровки.
Они созданы лишь для проверки и подтверждения информации.
(На примере показана криптографическая хеш-функция sha256, но в библиотеке hashlib также есть и другие, наподобие md5, sha512 и т.д.)

      Message: secret
Final message: 2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b
"""

from hashlib import sha256


def encrypt(string):
    signature = sha256(string.encode()).hexdigest()
    return signature


staticPassword = encrypt("secret")
dinamicPassword = encrypt(input("Write the password: "))

if staticPassword == dinamicPassword:
    print("Password is True!")
else:
    print("Password is False!")
