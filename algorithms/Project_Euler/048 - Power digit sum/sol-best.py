"""
Сумма 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.

  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0015154  0.152%              1000   9110846700 (ответ)
  2  0.0198508  1.834%             10000   6237204500
  3  0.247869   22.802%           100000   3031782500
"""


def solution(n=1000):
    """Находит последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + n^n.

    Использовано свойство модульной арифметики:
        (a+b) % c = ((a % c) + (b % c) )% c
    """
    c = 10 ** 10
    return sum(a ** a % c for a in range(1, n+1)) % c


def solution2(n=1000):
    """Находит последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + n^n.
    """
    MOD = 10 ** 10
    return sum(pow(i, i, MOD) for i in range(1, n+1)) % MOD


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution2, [1000, 10000, 100000])