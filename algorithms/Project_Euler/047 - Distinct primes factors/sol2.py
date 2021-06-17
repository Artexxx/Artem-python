"""
Первые два последовательные числа, каждое из которых имеет два отличных друг от друга простых множителя:

14 = 2 × 7
15 = 3 × 5

Первые три последовательные числа, каждое из которых имеет три отличных друг от друга простых множителя:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Найдите первые четыре последовательных числа, каждое из которых имеет четыре отличных друг от друга простых множителя. Каким будет первое число?

  Время  Замедление    Аргумент      Результат
-------  ------------  ----------  ----------- <12501 function calls>
  0.193  19,332%               4       134043 (Ответ)
"""

def solution(LIMIT=10**6):
    """Находит первое из первых четырех последовательных чисел, каждое из которых имеет четыре отличных друг от друга простых множителя.
    """
    sieve = [0] * (LIMIT+1)
    len_sequence = 0

    for n in range(2, LIMIT+1):
        if sieve[n] == 0:  # n is prime
            sieve[n::n] = [x + 1 for x in sieve[n::n]]
        if sieve[n] == 4:
            len_sequence += 1
            if len_sequence == 4:
                return n - 3  # нужно первое число
        else:
            len_sequence = 0

if __name__ == '__main__':

    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    import cProfile
    with cProfile.Profile() as pr:
        TimeProfile(solution)
    pr.print_stats()
