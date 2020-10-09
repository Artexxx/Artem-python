"""
Круговые простые числа
Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.

Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

Сколько существует круговых простых чисел меньше миллиона?

  №    Время  Замедление      Число    Результат
---  -------  ------------  -------  -----------
  1    1.508  150.800%      1000000           55
"""
import sys; sys.path.append('../..')
from number_base_alg import bit_sieve, is_prime


def is_circular_prime(n: int, n_is_prime: bool) -> bool:
    def rotations(chars: str) -> str:
        for i in range(len(chars)):
            yield int(chars[i:] + chars[:i])

    if not n_is_prime: return False
    for r in rotations(str(n)):
        if not is_prime(r): return False
    return True


def solution(N=1000000):
    """
    Возращает количество круговых простых чисел меньше миллиона.

    >>> solution()
    55
    """
    sieve_bit_array = bit_sieve(N)
    return sum(1 for n in range(3, N, 2) if is_circular_prime(n, sieve_bit_array[n])) + 1


if __name__ == '__main__':
    print(solution(int(input())))
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10**6])
