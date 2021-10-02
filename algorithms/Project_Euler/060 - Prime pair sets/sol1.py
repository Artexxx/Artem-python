"""
Объединение пары в простое число
Простые числа 3, 7, 109 и 673 достаточно замечательны.
Если взять любые два из них и объединить их в произвольном порядке, в результате всегда получится простое число.
Например, взяв 7 и 109, получатся простые числа 7109 и 1097.
Сумма этих четырех простых чисел, 792, представляет собой наименьшую сумму элементов множества из четырех простых чисел, обладающих данным свойством.

Найдите наименьшую сумму элементов множества из 5 простых чисел, для которых объединение любых двух даст новое простое число.

Результат:
    [13, 5197, 5701, 6733, 8389]
    # 3149980 function calls (3147535 primitive calls) in 2.128 seconds
"""
import math
from functools import lru_cache
from typing import List, Tuple, Iterable


def prime_sieve(n) -> Tuple[int]:
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

    return tuple(num for num in range(3, n + 1, 2) if sieve[num])


@lru_cache(maxsize=None)
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


@lru_cache(maxsize=None)
def is_concat_prime(x, y):
    """Возвращает True, если объединение двух простых чисел даст новое простое число"""
    return is_prime(int(str(x) + str(y)))


class solution():
    DEBUG = False
    MAX_ITER = 10000

    def __init__(self, max_chain_length=4):
        self.max_chain_length = max_chain_length
        self.primes: Tuple[int] = prime_sieve(self.MAX_ITER)


    def get_result(cls):
        """
        Возвращает наименьшую сумму элементов множества из N простых чисел, для которых объединение любых двух даст новое простое число.
        """
        return cls.solve_backtrack(chain=[])

    @staticmethod
    def test_chain(chain: Iterable[int], candidate: int) -> bool:
        for n in chain:
            if not is_concat_prime(n, candidate):
                return False
            if not is_concat_prime(candidate, n):
                return False
        return True

    def solve_backtrack(self, chain: List[int]):
        if self.DEBUG:
            print(self.max_chain_length, chain)

        for p in self.primes:
            if self.test_chain(chain, p):
                chain.append(p)
                if (len(chain) == self.max_chain_length):
                    return chain
                self.solve_backtrack(chain)
                chain.pop()
        return chain



if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import cProfile
    with cProfile.Profile() as pr:
        print(solution(5).get_result())
        print('\n\n');
        pr.print_stats()
