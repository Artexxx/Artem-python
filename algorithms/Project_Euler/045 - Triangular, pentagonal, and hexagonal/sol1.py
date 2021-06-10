"""
Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:

Треугольные	 	T(n) = n(n+1)/2 	1, 3, 6, 10, 15, ...
Пятиугольные	P(n) = n(3n-1)/2 	1, 5, 12, 22, 35, ...
Шестиугольные	H(n) = n(2n-1) 	 	1, 6, 15, 28, 45, ...

Можно убедиться в том, что T(285)= P(165) = H(143) = 40755.

Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным.
"""

def solution():
    """
    Возращает следующее треугольное число, являющееся также пятиугольным и шестиугольным.
    >>> solution()
    ...: 1533776805
    """

    def is_pentagonal(num):
        n = int((2 * num / 3) ** 0.5) + 1
        return n * (3 * n - 1) / 2 == num

    def is_triangle(num):
        n = ((1 + 8 * num)**0.5 - 1) / 2
        return n == int(n)

    index = 285
    while True:
        index += 4
        hexagonal = index * (2 * index - 1)
        if is_pentagonal(hexagonal) and is_triangle(hexagonal):
            return hexagonal


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import my_time_this
    my_time_this(solution)
