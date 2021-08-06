"""
Идеальным числом называется число, у которого сумма его делителей равна самому числу. Например, сумма делителей числа `28`
 равна `1 + 2 + 4 + 7 + 14 = 28`, что означает, что число `28` является идеальным числом.

Число `n` называется недостаточным, если сумма его делителей меньше `n`, и называется избыточным, если сумма его делителей больше `n`.

Так как число `12` является наименьшим избыточным числом (`1 + 2 + 3 + 4 + 6 = 16`), наименьшее число, которое может быть
записано как сумма двух избыточных чисел, равно 24. Используя математический анализ, можно показать, что все целые числа больше
`28123 `могут быть записаны как сумма двух избыточных чисел. Эта граница не может быть уменьшена дальнейшим анализом,
даже несмотря на то, что наибольшее число, которое не может быть записано как сумма двух избыточных чисел, меньше этой границы.

Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел.

  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0084076  0.841%              1000       240492
  2  0.466129   45.772%            28124      4179871 <4689078 function calls>
"""


def solution2(LIMIT=28124) -> int:
    """ Возвращает сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел
    """
    LIMIT = LIMIT + 1  # Fixme
    sum_divs = [0] * LIMIT
    # Находим сумму собственных делителей для каждого числа
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            sum_divs[j] += i

    abundants = set()
    result_sum = 0
    for n in range(1, LIMIT):
        # if n is abundant number
        if sum_divs[n] > n:
            abundants.add(n)

        if not any((n - a in abundants) for a in abundants):
            result_sum += n
    return result_sum


def return_deviders(number):
    deviders_list = []
    for i in range(1, int(number ** 0.5) + 1):
        if not number % i:
            deviders_list.append(i)
            if number // i not in deviders_list and number // i != number:
                deviders_list.append(number // i)
    return deviders_list


    def get_abundant_numbers():
        abundant_numbers_list = []
        for i in range(1, limit):
            if sum(return_deviders(i)) > i:
                abundant_numbers_list.append(i)
        return abundant_numbers_list

def solution(limit):


    abundants_sum = [False] * (limit + 1)
    abundant_numbers = get_abundant_numbers()

    for number_1 in abundant_numbers:
        for number_2 in abundant_numbers:
            if number_1 + number_2 <= limit:
                abundants_sum[number_1 + number_2] = True
            else:
                break

    return  sum(i for (i, position) in enumerate(abundants_sum) if not position)

if __name__ == '__main__':
    ## Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile; import cProfile
    TimeProfile(solution, [1000, 28124])
    with cProfile.Profile() as pr:
        solution(28124)
        print('\n\n');pr.print_stats()
