"""
Рассмотрим все целочисленные комбинации a^b для 2 ≤ a ≤ 5 и 2 ≤ b ≤ 5:

2^2=4,  2^3=8,   2^4=16,  2^5=32
3^2=9,  3^3=27,  3^4=81,  3^5=243
4^2=16, 4^3=64,  4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125

Если их расположить в порядке возрастания, исключив повторения,
мы получим следующую последовательность из 15 различных членов:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

Сколько различных членов имеет последовательность a^b для
 2 <= a <= 100 и 2 <= b <= 100?


  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.0054298  0.543%           1000       977358
  2  0.182178   17.67%          10000     99347607
  3  5.86805    568.59%        100000   9981236306
"""


def distinctProducts(n, m):
    """
    Возрощает количество различных произведений a и b для  1<=a<=n и 2<=b<=m
    >>> distinctProducts(1, 5)
    4
    >>> distinctProducts(2, 5)
    7   # 1:(2, 3, 4, 5) 2:({2}, {4}, 6, 8, 10)

    """
    set_products = set()

    for a in range(1, n + 1):
        for b in range(2, m + 1):
            set_products.add(a * b)
    return len(set_products)


def distinctPowers(n):
    """Возращает количество различных членов в последовательности, сгенерированной 2 <= a <= N и 2 <= b <= N

      >>> solution(100)
      9183
      >>> solution(50)
      2184
      >>> solution(20)
      324
      >>> solution(5)
      15
      >>> solution(2)
      1
      >>> solution(1)
      0
    """
    imperfect_powers = [True] * (n + 1)
    root = int(n ** 0.5)
    n_distinct = checked = 0
    for a in range(2, root + 1):
        if imperfect_powers[a]:
            max_power = 1
            a_pow = a ** 2
            while a_pow <= n:
                imperfect_powers[a_pow] = False
                max_power += 1
                a_pow *= a
            n_distinct += distinctProducts(max_power, n)
            checked += max_power
    n_distinct += (n - 1) * (n - checked - 1)
    return n_distinct


if __name__ == '__main__':
    print(distinctPowers(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(distinctPowers, [100, 1000, 10000])
