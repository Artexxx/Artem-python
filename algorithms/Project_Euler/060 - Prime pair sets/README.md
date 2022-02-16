# [Объединение пары в простое число](TODO)
## [Проблема](https://euler.jakumo.org/problems/view/60.html)

>Простые числа 3, 7, 109 и 673 достаточно замечательны. Если взять любые два из них и объединить их в произвольном порядке, в результате всегда получится простое число. Например, взяв 7 и 109, получатся простые числа 7109 и 1097. Сумма этих четырех простых чисел, 792, представляет собой наименьшую сумму элементов множества из четырех простых чисел, обладающих данным свойством.
>
>Найдите наименьшую сумму элементов множества из 5 простых чисел, для которых объединение любых двух даст новое простое число.
 
``` python
solution  (5) => 26033 # sum(13, 5197, 5701, 6733, 8389)
```

## Частное решение (1)


```python
import math
from typing import List, Iterable


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
    # number_of_multiples = len(sieve[4::2]) # old code ─ slow version
    number_of_multiples = (limit - 4 + limit % 2) // 2
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            # number_of_multiples = len(sieve[factor * factor::2*factor]) # old code ─ slow version
            number_of_multiples = ((limit - factor * factor - 1) // (2 * factor) + 1)
            sieve[factor * factor::factor * 2] = [False] * number_of_multiples
    return sieve


def prime_sieve(limit) -> List[int]:
    from itertools import compress
    sieve = bit_sieve(limit)
    return [2, *compress(range(3, limit, 2), sieve)]


def is_prime(n: int) -> bool:
    """
    Determines if the natural number n is prime.

    Example
    =======
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
    if n <= 3:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False

    # search for subsequent prime factors around multiples of 6
    max_factor = int(math.sqrt(n))
    for i in range(5, max_factor + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def custom_memoize(f):
    cache = {}

    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)
            cache[args[::-1]] = cache[args]
        return cache[args]

    return wrapper


@custom_memoize
def is_concat_prime(x, y):
    """
    Возвращает True, если при объединение в произвольном порядке x и y, в результате всегда получается простое число.
    """
    return (is_prime(int(str(x) + str(y))) and
            is_prime(int(str(y) + str(x))))


class PrimePairChain():
    PrimeLimit = 10_000

    def __init__(self, max_chain_length=4):
        self.max_chain_length = max_chain_length
        self._primes: List[int] = prime_sieve(self.PrimeLimit)

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
        return True

    def solve_backtrack(self, chain: List[int]):
        for p in self._primes:
            if self.test_chain(chain, p):
                chain.append(p)
                if len(chain) == self.max_chain_length:
                    return chain
                self.solve_backtrack(chain)
                chain.pop()
        return chain


def solution(N):
    """
    Возвращает наименьшую сумму элементов множества из N простых чисел, для которых объединение любых двух даст новое простое число.

    >>> solution(4)
    792 # sum([3, 7, 109, 673])
    >>> solution(5)
    26033 # sum([13, 5197, 5701, 6733, 8389])
    """
    result = PrimePairChain(N).get_result()
    return result
```
```text
26033
# 3149980 function calls (3147535 primitive calls) in 2.128 seconds
```
