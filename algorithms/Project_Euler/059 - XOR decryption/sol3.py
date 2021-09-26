"""
Каждый символ в компьютере имеет уникальный код, предпочитаемым является стандарт ASCII (American Standard cipher_text for Information Interchange - Американский стандартный код для обмена информацией).
Для примера, A верхнего регистра = 65, звездочка (*) = 42, а k нижнего регистра = 107.

Современный метод шифровки состоит в том, что берется текстовый файл, конвертируется в байты по ASCII, а потом над каждым
  байтом выполняется операция XOR с определенным значением, взятым из секретного ключа.
Преимущество функции XOR состоит в том, что применяя тот же ключ к зашифрованному тексту, получается исходный;
  к примеру, 65 XOR 42 = 107, тогда 107 XOR 42 = 65.

Для невзламываемого шифрования ключ должен быть такой же длины, что и сам текст, и ключ должен быть составлен из случайных байтов.
Тогда, если пользователь хранит зашифрованное сообщение и ключ шифрования в разных местах, то без обеих "половинок" расшифровать сообщение просто невозможно.

К сожалению, этот метод непрактичен для большинства пользователей, поэтому упрощенный метод использует в качестве ключа пароль.
Если пароль короче текстового сообщения, что наиболее вероятно, то ключ циклично повторяется на протяжении всего сообщения.
Идеальный пароль для этого метода достаточно длинный, чтобы быть надежным, но достаточно короткий, чтобы его можно было запомнить.

Ваша задача была упрощена, так как пароль состоит из трех символов нижнего регистра. Используя cipher1.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), содержащий зашифрованные коды ASCII, а также тот факт, что сообщение должно содержать распространенные английские слова, расшифруйте сообщение и найдите сумму всех значений ASCII в исходном тексте.

Result message: An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.
   Время  Замедление	Аргумент	  Результат
--------  ------------  ----------  -----------
0.000844  0.084%						 129448
"""
from collections import defaultdict
from typing import Tuple, List


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


if __name__ == '__main__':
	## Run Time-Profile Table ###
	import sys;	sys.path.append('..')
	from time_profile import TimeProfile
	TimeProfile(solution)
