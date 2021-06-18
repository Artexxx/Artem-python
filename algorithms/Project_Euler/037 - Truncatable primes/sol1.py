"""
Укорачиваемые простые числа
Число 3797 обладает интересным свойством.
Будучи само по себе простым числом, из него можно последовательно выбрасывать цифры слева направо, число же при этом остается простым на каждом этапе: 3797, 797, 97, 7.
Точно таким же способом можно выбрасывать цифры справа налево: 3797, 379, 37, 3.

Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как справа налево, так и слева направо, но числа при этом остаются простыми.

ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.

  №    Время  Замедление      Число    Результат
---  -------  ------------  -------  ----------- <859310 function calls>
  1  1.20824  120.824%           11       748317 (ответ)
"""
import math


def is_prime(n: int) -> bool:
    """
    Determines if the natural number n is prime.

    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
    # simple test for small n: 2 and 3 are prime, but 1 is not
    if n <= 3:
        return n > 1

    # check if multiple of 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # search for subsequent prime factors around multiples of 6
    max_factor = int(math.sqrt(n))
    for i in range(5, max_factor + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_truncable_prime(num):
    count_dig = len(str(num)) - 1
    div = 10
    for _ in range(count_dig):
        if not (is_prime(num % div) and is_prime(num // div)):
            return False
        div *= 10
    return True


def solution():
    """
    Возращает сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как справа налево, так и слева направо, но числа при этом остаются простыми.

    >>> solution()
    748317 # = {23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397}
    """
    result_sum = 0
    count_truncable_primes = 0
    temp_candidate = 23
    while count_truncable_primes != 11:
        if is_prime(temp_candidate) and is_truncable_prime(temp_candidate):
            count_truncable_primes += 1
            result_sum += temp_candidate
        temp_candidate += 2
    return result_sum


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    from cProfile import Profile
    with Profile() as pr:
        solution()
        pr.print_stats()
