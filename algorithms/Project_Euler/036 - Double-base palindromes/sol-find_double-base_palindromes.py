"""
Десятичное число `585 = 1001001001` (в двоичной системе), является палиндромом по обоим основаниям.

Найдите N число, являющиеся палиндромом по основаниям 10 и 2.

Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).


  №      Время  Замедление      Число      Результат
---  ---------  ------------  -------  -------------
  1  6.74e-05   0.007%             10            717
  2  0.0033971  0.33%              20        1758571
  3  0.102066   9.87%              30      939474939
  4  4.78291    468.08%            40  1413899983141
"""
def make_odd_bit_palindrome(x: int) -> str:
    res = x
    base = 2
    while (x > 0):
        res = res * base + x % base
        x = x // base
    return str(res)


def make_not_odd_bit_palindrome(x: int, middle_bit: int) -> str:
    binary_x = bin(x)[2:]
    pal = binary_x + str(middle_bit) + binary_x[::-1]
    return str(int(pal, 2))


def is_b10_palindrome(s: str) -> bool:
    """True, если n-десятичный палиндром"""
    return s == s[::-1]


def solution(N):
    if N == 1: return 1
    count = 1
    p_size = 1
    while True:
        # min и max с каждым проходом цикла будут увеличиваться на один разряд в двоичном виде
        min_bin_size = 2 ** (p_size - 1)
        max_bin_size = (2 ** p_size)
        for i in range(min_bin_size, max_bin_size):
            # Генерируем палиндром с четным кол-вом знаков в двоичном виде
            pal_candidate = make_odd_bit_palindrome(i)
            if is_b10_palindrome(pal_candidate):
                count += 1
                if (count == N): return pal_candidate

        for i in range(min_bin_size, max_bin_size + 1):
            for middle_bit in [0, 1]:
                # Генерируем палиндром с нечетным кол-вом знаков в двоичном виде
                pal_candidate = make_not_odd_bit_palindrome(i, middle_bit)
                if is_b10_palindrome(pal_candidate):
                    count += 1
                    if (count == N): return pal_candidate
        p_size += 1


if __name__ == '__main__':
    solution(50)