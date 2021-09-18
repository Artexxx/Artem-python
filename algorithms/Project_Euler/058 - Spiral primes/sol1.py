"""
Спиральные простые числа
Начиная с 1 и продвигаясь по спирали в направлении против часовой стрелки, получается квадратная спираль с длиной стороны 7

37 36 35 34 33 32 31     37             31
38 17 16 15 14 13 30        17       13
39 18  5  4  3 12 29           5   3
40 19  6  1  2 11 28             1
41 20  7  8  9 10 27           7   9
42 21 22 23 24 25 26        21       25
43 44 45 46 47 48 49     43             49

Интересно заметить, что нечетные квадраты лежат на правой нижней полудиагонали.
Еще интереснее то, что среди 13 чисел, лежащих на обеих диагоналях, 8 являются простыми; т.е. отношение составляет 8/13 ≈ 62%.
Если добавить еще один целый слой вокруг изображенной выше спирали, получится квадратная спираль с длиной стороны 9.
Если продолжать данный процесс, какой будет длина стороны квадратной спирали, у которой отношение количества простых чисел к
 количеству всех чисел на обеих диагоналях упадет ниже 10%?

  №     Время  Замедление      Аргумент    Результат
---  --------  ------------  ----------  -----------
  1  0.000657  0.066%               0.2          309
  2  1.59313   159.247%             0.1        26241 (Ответ)
"""
import math


def is_prime(n: int) -> bool:
    """
    Determines if the natural number n is prime.

    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
    # simple test for small n: 2 and 3 are prime, but 1 is not
    if n <= 3:
        return n > 1

    # check if multiple of 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # search for subsequent prime factors around multiples of 6
    max_factor = int(math.sqrt(n))
    for i in range(5, max_factor + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def solution(proportion=0.1):
    """
    Возвращает длину стороны квадратной спирали, у которой отношение количества простых чисел к количеству всех чисел на обеих диагоналях ниже 10%.

    Идея из решения 28 проблемы:
        Рассмотрим спираль, приведенную в примере.

        │ digit │ Index │
        │ ----- │ ----- │
        │ 1     │ 0     │
        │ 3     │ 2     │
        │ 5     │ 4     │
        │ 7     │ 6     │
        │ 9     │ 8     │
        │ 13    │ 12    │
        │ 17    │ 16    │
        │ 21    │ 20    │
        │ 25    │ 24    │

        При прохождении каждого квадрата индекс нужного числа увеличивается на 2, потом на 4, потом на 6..., до тех пор,
          пока мы не достигнем цифры, завершающей сетку.

    Примечание:
        Только первые 3 диагонали содержат простые числа
    """
    number = 1
    step = 2
    count_primes = 0
    count_diagonals_numbers = 1
    while True:

        # Только первые 3 диагонали содержат простые числа
        for i in range(0, 3):
            number += step
            if is_prime(number):
                count_primes += 1

        step += 2
        count_diagonals_numbers += 4

        if count_primes / count_diagonals_numbers < proportion:
            side_length = int(number ** 0.5)
            return side_length


if __name__ == '__main__':
    ## Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile;
    import cProfile

    TimeProfile(solution, [0.2, 0.1])
    with cProfile.Profile() as pr:
        solution(0.1)
        print('\n\n');
        pr.print_stats()
