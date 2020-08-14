"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5,то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.


 №       Время   Замедление        Число           Результат
---  ----------  ------------  ----------  ------------------
  1   0.0035757  0.358%            100000          2333316668
  2   0.0360629  3.25%            1000000        233333166668
  3   0.35144    31.54%          10000000      23333331666668
  4   3.49214    314.07%        100000000    2333333316666668
  5  34.0755     3058.33%      1000000000  233333333166666668
"""


def solution(number):
    """
    Возвращает сумму всех чисел, кратных 3 или 5 ниже n.
    [*] Это решение основано на паттерне: 0+3,+2,+1,+3,+1,+2,+3.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    """
    result_sum = 0
    counter = 0
    while 1:
        counter += 3
        if counter >= number:
            break
        result_sum += counter
        counter += 2
        if counter >= number:
            break
        result_sum += counter
        counter += 1
        if counter >= number:
            break
        result_sum += counter
        counter += 3
        if counter >= number:
            break
        result_sum += counter
        counter += 1
        if counter >= number:
            break
        result_sum += counter
        counter += 2
        if counter >= number:
            break
        result_sum += counter
        counter += 3
        if counter >= number:
            break
        result_sum += counter
    return result_sum


if __name__ == "__main__":
    print(solution(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000])
