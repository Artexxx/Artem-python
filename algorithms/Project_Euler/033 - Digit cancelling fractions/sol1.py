from timeit import default_timer


def ReducedFraction(n, d):
    """
    Принимает дробь в виде кортежа (числитель,знаменатель) и возвращает сокращенную форму дроби.

    [*] Для сокращения дроби, используется, "Алгоритм Евклида" - для нахождения общего делителя.
    """

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common_divisor = gcd(n, d)
    return (n // common_divisor, d // common_divisor)


def cancel_digit(numerator, denominator):
    """
    Сокращает общую цифру в числителе и знаменателе (игнорирует 0)
    """
    numerator_digits_set = set(str(numerator))
    denominator_digits_set = set(str(denominator))
    if (('0' not in numerator_digits_set | denominator_digits_set) and
        (len(numerator_digits_set) > 1) and(len(denominator_digits_set) > 1)):
        common_digit = numerator_digits_set & denominator_digits_set
        if common_digit:
            repeat = common_digit.pop()
            numerator_cancelled = str(numerator).replace(repeat, '')
            denominator_cancelled = str(denominator).replace(repeat, '')
            return (int(numerator_cancelled), int(denominator_cancelled))
    return None


def solution():
    """
    Возвращает знаменатель произведения 4x особых дробей.

    >>> solution()
    100
    """
    result_fractions = []
    for denominator in range(12, 99):
        for numerator in range(12, denominator):
            canceled_fraction = cancel_digit(numerator, denominator)
            digits_is_canceled = canceled_fraction is not None
            if digits_is_canceled:
                arithmetics_reduced = ReducedFraction(numerator, denominator)
                if ReducedFraction(*canceled_fraction) == arithmetics_reduced:
                    result_fractions.append(arithmetics_reduced)
    product_numerators, product_denominators = (1, 1)
    for (n, d) in result_fractions:
        product_numerators *= n
        product_denominators *= d
    return ReducedFraction(product_numerators, product_denominators)[1]


if __name__ == '__main__':
    start_time = default_timer()
    answer = solution()
    end_time = default_timer()
    print("The denominator is {} and it took {:f} seconds to find.".format(answer, end_time - start_time))
