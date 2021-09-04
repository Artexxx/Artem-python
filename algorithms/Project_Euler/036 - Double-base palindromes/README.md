# [Двухосновные палиндромы](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/35.html)

>Десятичное число `585 = 1001001001` (в двоичной системе), является палиндромом по обоим основаниям.
>
>Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.
>
>(Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).

``` python
solution  (100)  # => 157 # [1, 3, 5, 7, 9, 33, 99]

solution  (10**6)  # => 872187 # [1, 3, 5, 7, 9, 33, 99, 313, 585, 717, 7447, 9009, 15351, 32223, 39993, 53235, 53835, 73737, 585585]
```


## Частное решение (1)


[#] палиндром по основанию два должен быть нечетным, поскольку он не может иметь ведущего нуля. 
Это вдвое сокращает пространство поиска.

```python
def is_double_base_palindrome(num: int) -> bool:
    """
    Возвращает True, если число `num` по основанию {10} и {2} является полиндромом.
    num (int) - натуральное число в 10 системе счисления
    >>> is_double_base_palindrome(585)
    True #585 = 1001001001 (binary)
    """
    num_str = str(num)
    bin_num_str = bin(num)[2:]
    return num_str == num_str[::-1] and bin_num_str == bin_num_str[::-1]


def solution(N=10 ** 6):
    """
    Возвращает сумму двухосновных палиндромов меньше миллиона.

    >>> solution(10**6)
    872187
    """
    return sum(n for n in range(3, N, 2)
               if is_double_base_palindrome(n)) + 1
```
```
  №       Время  Замедление        Число    Результат
---  ----------  ------------  ---------  -----------
  1   0.0022488  0.225%             10000       18228
  2   0.231982   22.97%         1_000_000      872187 <Ответ>
  3  23.9195     2368.76%     100_000_000    39347399
 ```

## Частное решение (2)
```python
def make_bit_palindrome(x: int, base: int, oddPalindrome: bool) -> int:
    """Создаёт 10-тичное число, которое палиндром в 2-й системе, дублируюя x в 2-ой; если x c нечетным количеством знаков, то `средний бит` пропускается

    5 - 101 (binary)
    >>> make_bit_palindrome(5, 2, oddPalindrome=False)
    45 # 101101 (binary)
    
    585 - 1001001001 (binary)
    >>> make_bit_palindrome(585, 2, oddPalindrome=False)
    599625 # 0b10010010011001001001 (binary)
    
    251 - 11111011 (binary)
    >>> make_bit_palindrome(251, 2, oddPalindrome=True)
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
    Возвращает сумму двухосновных палиндромов меньше миллиона.

    >>> solution(10**6)
    872187
    """
    result_sum = 0
    for odd in (True, False):
        for n in itertools.count(1):
            pal_candidate = make_bit_palindrome(n, 2, odd)
            if pal_candidate >= LIMIT: break
            if is_b10_palindrome(pal_candidate):
                result_sum += pal_candidate
    return result_sum
```
```text
  №      Время  Замедление            Число      Результат
---  ---------  ------------  -------------   ------------
  1  0.0032022  0.320%              10 00000        872187 <Ответ>
  2  0.0409729  3.78%             100 000000      39347399
  3  0.529231   48.83%          10000 000000   11351036742
  4  6.08442    555.52%      1 000000 000000  394832891346
```

## Аналогичная задача (1)

>Десятичное число `585 = 1001001001` (в двоичной системе), является палиндромом по обоим основаниям.
>
>Найдите N число, являющиеся палиндромом по основаниям 10 и 2.
>
>(Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).


| №   | Палиндром |
|---- | ------ |
| 1   | 1        |
| 2   | 3        |
| 3   | 5        |
| 4   | 7        |
| 5   | 9        |
| 6   | 33       |
| 7   | 99       |
| 8   | 313      |
| 9   | 585      |
| 10  | 717      |
| 11  | 7447     |
| 12  | 9009     |
| 13  | 15351    |
| 14  | 32223    |

```python
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
```