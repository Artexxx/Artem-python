"""
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе n!.
"""

from functools import reduce
solution1 = lambda n: reduce(int.__add__, map(int, str(reduce(int.__mul__, map(int, range(1, n))))))
assert solution1(100) == 648

from math import factorial
solution2 = lambda n: sum(map(int, str(factorial(n))))
assert solution2(100) == 648

print('[+] Tests Ok')
