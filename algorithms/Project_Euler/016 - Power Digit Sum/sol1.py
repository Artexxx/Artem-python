"""
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^power?
"""


def solution(power):
    """Возвращает сумму цифр числа 2^power.

    >>> solution(1000)
    1366
    >>> solution(50)
    76
    >>> solution(20)
    31
    >>> solution(15)
    26
    """
    num = 2 ** power
    string_num = str(num)
    list_num = list(string_num)
    sum_of_num = 0

    for i in list_num:
        sum_of_num += int(i)
    return sum_of_num


def solution2(power):
    """Аналогичное решение, без использования строк"""
    num = 2 ** power
    result_num = 0
    while num:
        result_num, num = result_num + num % 10, num // 10
    return result_num


solution3 = lambda n: sum(map(int, str(2 ** n)))

if __name__ == "__main__":
    power = int(input("Enter the power of 2: ").strip())
    print("2 ^", power, " = ", 2 ** power)
    result = solution3(power)
    print("Sum of the digits is: ", result)
