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


def solution():
    result_sum = 0
    powers = {str(d): d ** 5 for d in range(10)}

    for digits in combinations_with_replacement('0123456789', 6):
        candidate = sum(powers[d] for d in digits)
        check_sum = sum(powers[d] for d in str(candidate))
        if candidate == check_sum:
            result_sum += candidate

    return result_sum - 1  # As 1 = 1^n is not a sum it is not included.


if __name__ == "__main__":
    import cProfile
    with cProfile.Profile() as p:
        print(solution())
    p.print_stats()


