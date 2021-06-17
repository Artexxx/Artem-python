"""
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе n!.
"""
from cProfile import Profile
from functools import reduce
from operator import add, mul
solution1 = lambda n: reduce(add, map(int, str(reduce(mul, map(int, range(1, n))))))
assert solution1(100) == 648

from math import factorial
solution2 = lambda n: sum(map(int, str(factorial(n))))
assert solution2(100) == 648

print('[+] Tests Ok')
