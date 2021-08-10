"""
Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.

Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.
"""
from itertools import combinations_with_replacement
from types import MappingProxyType


def solution(N):
    result_sum = 0
    powers = MappingProxyType({str(d): d ** N for d in range(10)})
    if N >= 5: N += 1

    for digits in combinations_with_replacement('0123456789', N):
        candidate = sum(powers[d] for d in digits)
        check_sum = sum(powers[d] for d in str(candidate))
        if candidate == check_sum:
            result_sum += candidate
    return result_sum - 1  # 1 = 1^4 не считается, так как это - не сумма.


if __name__ == "__main__":
    import cProfile
    with cProfile.Profile() as p:
        print(solution(5))
    p.print_stats()

