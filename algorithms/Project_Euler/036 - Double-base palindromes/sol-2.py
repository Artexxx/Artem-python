"""
Двухосновные палиндромы
Десятичное число 585 = 1001001001 (в двоичной системе), является палиндромом по обоим основаниям.

Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.

(Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).

  №      Время  Замедление            Число     Результат
---  ---------  ------------  -------------  ------------
  1  0.0032022  0.320%              1000000        872187
  2  0.0409729  3.78%             100000000      39347399
  3  0.529231   48.83%          10000000000   11351036742
  4  6.08442    555.52%       1000000000000  394832891346

"""
import itertools


def make_bit_palindrome(x: int, base: int, oddPalindrome: bool) -> int:
    """Создаёт 10-тичное число, которое палиндром в 2-ой системе, дублируюя x в 2-ой; если x c нечетным количеством знаков, то `средний бит` пропускается

    >>> make_bit_palindrome(5, 2, oddPalindrome=False) # 5 - 101 (binary)
    45 # 101101 (binary)

    >>> make_bit_palindrome(585, 2, oddPalindrome=False) # 585 - 1001001001 (binary)
    599625 # 0b10010010011001001001 (binary)

    >>> make_bit_palindrome(251, 2, oddPalindrome=True) # 251 - 11111011 (binary)
    32223 # 111110111011111 (binary)
    """
    res = x
    if oddPalindrome:
        x = x // base
    while (x > 0):
        res = res * base + x % base
        x = x // base
    return res


def is_b10_palindrome(n: int) -> bool:
    """True, если n-десятичный палиндром"""
    s = str(n)
    return s == s[::-1]


def solution(LIMIT=10 ** 6):
    """
    Возращает сумму двухосновных палиндромов меньше миллиона.

    >>> solution(10**6)
    872187
    """
    a=[]
    result_sum = 0
    for odd in (True, False):
        for n in itertools.count(1):
            pal_candidate = make_bit_palindrome(n, 2, odd)
            if pal_candidate >= LIMIT: break
            if is_b10_palindrome(pal_candidate):
                result_sum += pal_candidate
                a.append(pal_candidate)
    return result_sum


if __name__ == '__main__':
    print(solution())
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10 ** 6, 10 ** 8, 10 ** 10, 10 ** 12])
