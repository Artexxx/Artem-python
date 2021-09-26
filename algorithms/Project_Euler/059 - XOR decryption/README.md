# [XOR шифровка](TODO)
## [Проблема](https://euler.jakumo.org/problems/view/59.html)

>Каждый символ в компьютере имеет уникальный код, предпочитаемым является стандарт ASCII (American Standard Code for Information Interchange - Американский стандартный код для обмена информацией). Для примера, A верхнего регистра = 65, звездочка (*) = 42, а k нижнего регистра = 107.
>
>Современный метод шифровки состоит в том, что берется текстовый файл, конвертируется в байты по ASCII, а потом над каждым байтом выполняется операция XOR с определенным значением, взятым из секретного ключа. Преимущество функции XOR состоит в том, что применяя тот же ключ к зашифрованному тексту, получается исходный; к примеру, 65 XOR 42 = 107, тогда 107 XOR 42 = 65.
>
>Для невзламываемого шифрования ключ должен быть такой же длины, что и сам текст, и ключ должен быть составлен из случайных байтов. Тогда, если пользователь хранит зашифрованное сообщение и ключ шифрования в разных местах, то без обеих "половинок" расшифровать сообщение просто невозможно.
>
>К сожалению, этот метод непрактичен для большинства пользователей, поэтому упрощенный метод использует в качестве ключа пароль. Если пароль короче текстового сообщения, что наиболее вероятно, то ключ циклично повторяется на протяжении всего сообщения. Идеальный пароль для этого метода достаточно длинный, чтобы быть надежным, но достаточно короткий, чтобы его можно было запомнить.
>
>Ваша задача была упрощена, так как пароль состоит из трех символов нижнего регистра. Используя cipher1.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), содержащий зашифрованные коды ASCII, а также тот факт, что сообщение должно содержать распространенные английские слова, расшифруйте сообщение и найдите сумму всех значений ASCII в исходном тексте.

 
``` python
solution  () => 129448
```

## Частное решение (1)

```python

def split_text_to_key(cipher_text: Tuple[int], len_key=3):
	"""
	Разделяет текст на несколько колонок для каждого символа ключа

	>>> split_text_to_key('abcd12345', 3)
	[('a', 'd', '3'), ('b', '1', '4'), ('c', '2', '5')]
	"""
	result = []
	for letter_index in range(len_key):
		slice = range(letter_index, len(cipher_text), len_key)
		result.append(tuple(cipher_text[i] for i in slice))
	return result


def get_score(decrypted: List[int]):
	""" 
	Эвристическая функция, которая помогает узнать успешность расшифровки, чем больше результат, тем лучше. 
	"""
	result = 0
	for c in decrypted:
		if 65 <= c <= 90:  # Проверка 'a' - 'z'
			result += 1
		elif 97 <= c <= 122:  # Проверка 'A' - 'Z'
			result += 2
		elif c < 32 or c > 126:
			result -= 10
	return result


def decrypt_column(cipher_text: Tuple[int], letter_key: int):
	return tuple(c ^ letter_key for c in cipher_text)


def decrypt_message(cipher_text: Tuple[int], key: List[int]):
	len_key = len(key)
	result = []

	for (i, c) in enumerate(cipher_text):
		result.append(c ^ key[i % len_key])
	return result


def solution():
	raw_string = open('cipher.txt').read()
	cipher_text = tuple(map(int, raw_string.split(',')))
	encrypted_key = []

	for column in split_text_to_key(cipher_text):

		best_encrypted_letter = None
		best_score = 0

		for letter in map(ord, ascii_lowercase):
			decrypted = decrypt_column(column, letter)
			new_score = get_score(decrypted)
			if new_score > best_score:
				best_score = new_score
				best_encrypted_letter = letter

		encrypted_key.append(best_encrypted_letter)

	best_decrypted = decrypt_message(cipher_text, encrypted_key)
	print('Result message:', ''.join(map(chr, best_decrypted)))
	return sum(best_decrypted)
```
```text
    Время  Замедление    Результат
---------  ----------- -----------
0.0153283  1.533%           129448
```

## Частное решение (2)

Это решение основано на том, что пробел самый частый символ в тексте.

```python

def histogram(cipher_text: Tuple[int]):
	d = defaultdict(int)
	for c in cipher_text:
		d[c] = d[c] + 1
	return d


def decipher(cipher_text: Tuple[int]):
	h = histogram(cipher_text)
	spacecipher_text = max(h.items(), key=lambda pr: pr[1])[0]
	key = spacecipher_text ^ ord(' ')
	return key


def decrypt(cipher_text: Tuple[int], key: List[int]):
	len_key = len(key)
	result = []
	for (i, c) in enumerate(cipher_text):
		result.append(c ^ key[i % len_key])
	return result


def solution(key_size=3):
	"""
	Расшифровывает сообщение и возвращает сумму всех значений ASCII в исходном тексте.
	"""
	raw_string = open('cipher.txt').read()
	cipher_text = tuple(map(int, raw_string.split(',')))

	keys = [decipher(cipher_text[i::key_size]) for i in range(key_size)]
	decrypted = decrypt(cipher_text, keys)

	print('Result message:', ''.join(''.join(map(chr, decrypted))))
	return sum(decrypted)
```

```text

Result message: An extract taken from the introduction of one of Euler's [...]
   Время  Замедление	Аргумент	  Результат
--------  ------------  ----------  -----------
0.000844  0.084%						 129448
```