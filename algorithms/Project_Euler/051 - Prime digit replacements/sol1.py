"""
Замена цифр в простом числе
Меняя первую цифру числа *3 (двузначного числа, заканчивающегося цифрой 3),
 оказывается, что шесть из девяти возможных значений - 13, 23, 43, 53, 73 и 83 - являются простыми числами.

При замене третьей и четвертой цифры числа 56**3 одинаковыми цифрами, получаются десять чисел,
 из которых семь - простые: 56003, 56113, 56333, 56443, 56663, 56773 и 56993.
Число 56**3 является наименьшим числом, подставление цифр в которое дает именно семь простых чисел.
Соответственно, число 56003, будучи первым из полученных простых чисел, является наименьшим простым числом, обладающим указанным свойством.

Найдите наименьшее простое число, которое является одним из восьми простых чисел, полученных заменой части цифр (не обязательно соседних) одинаковыми цифрами.

   Время  Замедление    Аргумент      Результат
--------  ------------  ----------  -----------
0.230331  23.033%                        121313 <Ответ>
"""
import math
from collections import Counter
from string import digits


def prime_sieve(n):
    """ Sieve of Eratosthenes
     Generate boolean array of length N, where prime indices are True.

    The time complexity of this algorithm is O(nloglog(n).

    >>> prime_sieve(10)
    [2, 3, 5, 7]
    """
    sieve = [True] * n
    sieve[0], sieve[1] = False, False  # числа 0 и 1

    number_of_multiples = len(sieve[4::2])
    sieve[4::2] = [False] * number_of_multiples
    for factor in range(3, int(math.sqrt(n)) + 1, 2):
        if sieve[factor]:
            number_of_multiples = len(sieve[factor * factor::factor * 2])
            sieve[factor * factor::factor * 2] = [False] * number_of_multiples

    return (num for num in range(3, n + 1, 2) if sieve[num])


def count_duplicated_digits(number: int) -> int:
    return len(str(number)) - len(set(str(number)))


def get_duplicated_digits(number: str) -> str:
    """ Возвращает повторяющиеся цифры
    >>> list(get_duplicated_digits("1112333"))
    ['1', '3']
    """
    for digit, count in Counter(number).items():
        if count >= 3:
            yield digit


def get_patterns(number: int):
    """ Возвращает паттерны повторяющихся цифр
    >>> list(get_patterns(1112333))
    ['***2333', '1112***']
    """
    number = str(number)
    for digit in get_duplicated_digits(number):
        yield number.replace(digit, "*")


def get_candidates(pattern):
    for digit in digits:
        yield int(pattern.replace("*", digit))


def solution():
    """
    Находит наименьшее простое число, которое является одним из восьми простых чисел, полученных заменой части цифр (не обязательно соседних) одинаковыми цифрами.
    """
    fprimes = [prime for prime in prime_sieve(10 ** 6)
               if count_duplicated_digits(prime) >= 3]
    patterns_view = []
    for prime in fprimes:

        for pattern in get_patterns(prime):
            if pattern in patterns_view:
                continue
            primes_count = 0
            for candidate in get_candidates(pattern):
                if candidate in fprimes and (len(str(candidate)) == len(str(prime))):
                    primes_count += 1
            if primes_count == 8:
                return prime
            patterns_view.append(pattern)


if __name__ == '__main__':
    # ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution)