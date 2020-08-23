from functools import reduce
solution1 = lambda n: reduce(int.__add__, map(int, str(reduce(int.__mul__, map(int, range(1, n))))))
assert solution1(100) == 648

from math import factorial
solution2 = lambda n: sum(map(int, str(factorial(n))))
assert solution2(100) == 648

print('[+] Tests Ok')