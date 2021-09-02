"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – `9009` = 91 × 99.

Найдите самый большой палиндром, который меньше N и сделан из произведения двух 3-значных чисел.
"""


def is_palindromic(number: int) -> bool:
    reverse = 0
    i = number
    while i > 0:
        reverse = reverse * 10 + i % 10
        i //= 10
    return reverse == number


def solution(n):
    """Возвращает самый большой палиндром, который меньше N и сделан из произведения двух 3-значных чисел.

    >>> solution(20000)
    19591
    >>> solution(30000)
    29992
    >>> solution(40000)
    39893
    """
    for number in range(n - 1, 10000, -1):
        if is_palindromic(number):
            divisor = 999
            while divisor != 99:
                if (number % divisor == 0) and (len(str(int(number / divisor))) == 3):
                    print(divisor)
                    return number
                divisor -= 1
    return 'Palindrome not found'


if __name__ == "__main__":
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [20000, 100000, 1000000])
