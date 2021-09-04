"""
Возьмем число 192 и умножим его по очереди на 1, 2 и 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

Объединяя все три произведения, получим девятизначное число 192384576 из цифр от 1 до 9 (пан-цифровое число). Будем называть число 192384576 объединенным произведением 192 и (1,2,3)
Таким же образом можно начать с числа 9 и по очереди умножать его на 1, 2, 3, 4 и 5, что в итоге дает пан-цифровое число 918273645, являющееся объединенным произведением 9 и (1,2,3,4,5).
Какое самое большое девятизначное пан-цифровое число можно образовать как объединенное произведение целого числа и (1,2, ... , n), где n > 1?
"""


def is_pandigital(n):
    n = str(n)
    if len(n) == 9 and len(set(n)) == 9 and '0' not in n:
        return True
    return False


def find_product(num) -> int:
    """
    Возвращает девятизначное число, образованное как конкатенация строковых произведений целого числа и (1,2, ... , n), где n > 1.
    return: concatenating(num*1, num*2, num*3, ...  num*n)
    """
    result_product = ""
    result_len = 0
    i = 1
    while len(result_product) < 9:
        new_len = len(str(num * i))
        result_len += new_len
        if result_len > 9:
            break
        else:
            result_product += str(num * i)
        i += 1
    return int(result_product)


def solution():
    """
    Возвращает cамое большое девятизначное пан-цифровое число, образованное как объединенное произведение целого числа и (1,2, ... , n), где n > 1
    >>> solution()
    932718654 # 9327*(1,2,...,n)
    """
    max_pandigital = 0
    for num in range(9000, 9999+1):
        pandigital_candidate = find_product(num)
        if is_pandigital(pandigital_candidate):
            max_pandigital = max(pandigital_candidate, max_pandigital)
    return max_pandigital


if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    print(solution())
    print("Time: {:.5}ms".format(default_timer() - start_time))
