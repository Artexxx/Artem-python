"""
Гугол ((10)^100) - гигантское число: один со ста нулями; (100)^100 почти невообразимо велико: один с двумястами нулями.
Несмотря на их размер, сумма цифр каждого числа равна всего лишь 1.

Рассматривая натуральные числа вида (a)^b, где a, b < 100, какая встретится максимальная сумма цифр числа?

    №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0685827  6.858%               100          972 (Ответ)
  2  0.63083    56.225%              200         2205 <80000 function calls>>
"""


def solution(LIM=100):
    """
    Возвращает максимальную сумму цифр числа из чисел вида (a)^b, где a, b < `LIM`?
    """
    return max(
            sum(map(int, str(a ** b)))
            for a in range(LIM)
            for b in range(LIM)
    )



if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile;import cProfile
    TimeProfile(solution, [100, 200])
    with cProfile.Profile() as pr:
        solution(200)
    pr.print_stats()