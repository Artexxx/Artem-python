"""
Последовательность треугольных чисел образуется путем сложения натуральных чисел.
К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

Первые десять треугольных чисел: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Перечислим делители первых семи треугольных чисел:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

Каково первое треугольное число, у которого более N делителей?


  №      Время  Замедление      Число     Результат
---  ---------  ------------  -------  ------------
  1  0.0007446  0.074%             50         25200
  2  0.0065189  0.58%             250       2162160
  3  0.0424357  3.59%             500      76576500
  4  0.148476   10.60%           1000     842161320
  5  2.70428    255.58%          3000  102774672000
"""
import itertools, collections
import math


def memoize(f):
    cache = {}

    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)
            # print(f"[#] F(",int(*args), ')\t => \t', dict(cache[args])) # TEST OUTPUT
        return cache[args]

    return wrapper


@memoize
def prime_factorization(x):
    """
     >>> prime_factorization(220)
    {2: 2, 5: 1, 11: 1} # 2 * 2 * 5 * 11
    """
    for i in range(2, math.floor(math.sqrt(x) + 1)):
        if x % i == 0:
            old_factorization = prime_factorization(x / i).copy()
            old_factorization[i] += 1
            return old_factorization
    # Нет делителей -> x простое число
    res = collections.defaultdict(int)
    res[x] = 1
    return res


def merge_factors(f1, f2):
    res = f1.copy()
    for k, v in f2.items():
        res[k] += v
    return res


def num_factors(factorization):
    product = 1
    for v in factorization.values():
        product *= (v + 1)
    return product


def solution(N):
    for n in itertools.count(start=1):
        factors1 = prime_factorization(n / 2 if n % 2 == 0 else n)
        factors2 = prime_factorization(n + 1 if n % 2 == 0 else (n + 1) / 2)
        full_factorization = merge_factors(factors1, factors2)

        if num_factors(full_factorization) >= N:
            print("The first triangular number with {} divisors is {:,}".format(N, int(n * (n + 1) / 2)))
            return int(n * (n + 1) / 2)


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [50, 250, 500, 1000, 3000, ])
