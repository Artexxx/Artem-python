"""
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^power?
"""

solution = lambda n: sum(map(int, str(2 ** n)))


def solution2(power):
    """Аналогичное решение, без использования строк"""
    num = 2 ** power
    result_num = 0
    while num:
        result_num, num = result_num + num % 10, num // 10
    return result_num


if __name__ == "__main__":
    print(solution(int(input())))
