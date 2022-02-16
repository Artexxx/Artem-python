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
--------  ------------  ----------  ----------- <248858 function calls>
0.224035  22.403%                        121313 (Ответ)
"""
import cProfile
import math
from collections import Counter
from string import digits
from typing import Iterator, List


def bit_sieve(limit: int) -> bytearray:
    """
    Sieve of Eratosthenes
    Input limit>=3, return boolean array of length `limit`,
    where index is number and boolean values is whether prime or not
    The time complexity of this algorithm is O(nloglog(n).

    Example
    ========
    >>> list(bit_sieve(10))
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]

    Time-Profile
    ============
    ===  =========  ============  ===========  ============
      №       Time  Slowdown         Argument  Count primes
    ===  =========  ============  ===========  ============
      1  0.001174   0.118%            100_000          9592
      2  0.013186   1.201%          1_000_000         78498
      3  0.131736   11.855%        10_000_000        664579
      4  1.63013    149.840%      100_000_000       5761455
    ===  =========  ============  ===========  ============
    """
    sieve = bytearray([True]) * limit
    sieve[0] = False
    sieve[1] = False
    # old code ─ slow version
    # # old code ─ slow version
    # number_of_multiples = len(sieve[4::2])
    number_of_multiples = (limit - 4 + limit % 2) // 2
    number_of_multiples = (limit - 4 + limit % 2) // 2
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            # old code ─ slow version
            # number_of_multiples = len(sieve[factor * factor::2*factor])
            number_of_multiples = ((limit - factor * factor - 1) // (2 * factor) + 1)
            sieve[factor * factor::factor * 2] = [False] * number_of_multiples
    return sieve


def prime_sieve(limit) -> List[int]:
    """
    Input limit>=3, return a list of prime numbers less than `limit`.

    Example
    ========
    >>> prime_sieve(11)
    [2, 3, 5, 7, 11]
    >>> prime_sieve(17)
    [2, 3, 5, 7, 11, 13, 17]
    """
    from itertools import compress
    sieve = bit_sieve(limit+1)
    return [2, *compress(range(3, limit+1, 2), sieve[3::2])]


def count_duplicated_digits(number: int) -> int:
    return len(str(number)) - len(set(str(number)))


def get_duplicated_digits(number: str) -> str:
    """
    Возвращает повторяющиеся цифры

    >>> list(get_duplicated_digits("1112333"))
    ['1', '3']
    """
    for digit, count in Counter(number).items():
        if count >= 3:
            yield digit


def get_patterns(number: int):
    """
    Возвращает паттерны повторяющихся цифр

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
    Находит наименьшее простое число, которое является одним из восьми простых чисел,
    полученных заменой части цифр (не обязательно соседних) одинаковыми цифрами.

    >>> solution()
    121313
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
    with cProfile.Profile() as pr:
        solution()
    print(pr.print_stats())

