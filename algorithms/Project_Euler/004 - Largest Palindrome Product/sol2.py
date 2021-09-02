"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – `9009` = 91 × 99.

Найдите самый большой палиндром, сделаный из произведения двух n-значных чисел.


  №       Время  Замедление      Число    Результат
---  ----------  ------------  -------  -----------
  1   0.000237   0.024%              2         9009
  2   0.0345041  3.43%               3       906609
  3   0.301147   26.66%              4     99000099
  4  12.0154     1171.43%            5   9966006699
"""


def is_palindromic(number: int) -> bool:
    reverse = 0
    i = number
    while i > 0:
        reverse = reverse * 10 + i % 10
        i //= 10
    return reverse == number


def largest_palindrome_number(n):
    LargestNumber = int("9" * n)
    SmallestNumber = int("1" + "0" * (n - 1))

    for i in range(LargestNumber * LargestNumber, SmallestNumber * SmallestNumber, -1):
       if is_palindromic(i):
            for j in range(LargestNumber, SmallestNumber, -1):
                if (j * j < i):
                    break  # если J^2 меньше палиндрома, то проверять меньшие значения j бесполезно
                for k in range(j, SmallestNumber, -1):
                    if (j * k == i):
                        return i
                    elif (j * k < i):
                        break  # если произведение  меньше, то проверять меньшие значения k бесполезно
    return 'Palindrome not found'


if __name__ == '__main__':
    print(largest_palindrome_number(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(largestPalindromeProduct, [2, 3, 4, 5])
