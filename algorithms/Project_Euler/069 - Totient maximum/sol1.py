"""
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения количества чисел, меньших n, которые взаимно просты с n.
К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9)=6.

   n        Relatively Prime        φ(n)     n/φ(n)
   2        1                       1        2
   3        1,2                     2        1.5
   4        1,3                     2        2
   5        1,2,3,4                 4        1.25
   6        1,5                     2        3
   7        1,2,3,4,5,6             6        1.1666...
   8        1,3,5,7                 4        2
   9        1,2,4,5,7,8             6        1.5
   10       1,3,7,9                 4        2.5

Нетрудно заметить, что максимум n/φ(n) наблюдается при n=6, для n ≤ 10.
Найдите значение n ≤ 1 000 000, при котором значение n/φ(n) максимально.
"""


def solution(limit=10 ** 6):
    """
    Возвращает значение n ≤ limit, при котором значение n/φ(n) максимально.
    """
    phi = list(range(limit + 1))

    for p in range(2, len(phi)):
        if phi[p] == p:  # p is prime
            for i in range(2 * p, limit + 1, p):
                phi[i] -= phi[i] // p

    return max(range(2, limit + 1), key=(lambda i: i / phi[i]))


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [10 ** 4, 10 ** 5, 10 ** 6])
