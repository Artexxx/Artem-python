"""
Выписав первые шесть простых чисел, получим

    2, 3, 5, 7, 11, 13

Какое число является N-ым простым числом?


  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0153429  1.534%             10001       104743 (ответ)
  2  0.254947   23.960%           100001      1299721
  3  3.19012    293.517%         1000001     15485867
"""
import math


def bit_sieve(n) -> list:
    """
    Решето Эратосфена.
    Сложность: nloglog(n).
    """
    bits = [True] * (n + 1)
    for index in range(2, int(math.sqrt(n))):
        if bits[index]:  # если i - простое
            for j in range(index * index, n + 1, index):  # занулить все ему кратные
                bits[j] = False
    return bits


def solution(n):
    """Возвращает N-е простое число.

    >>> solution(10001)
    104743
    """
    # N-ое простое не превосходит 1,5 N ln( N ) при N > 1:
    sieve = bit_sieve(int(1.5 * n * math.log(n)) + 1)

    count_primes = 0
    index = 1
    while count_primes != n and index < 3:
        index += 1
        if sieve[index]:
            count_primes += 1
    while count_primes != n:
        index += 2
        if sieve[index]:
            count_primes += 1
    return index


if __name__ == "__main__":
    # print(solution(int(input().strip())))
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [10001, 100001, 1000001])
