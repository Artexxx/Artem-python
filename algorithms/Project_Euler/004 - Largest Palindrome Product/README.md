# [Наибольшее произведение-палиндром](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/4.html)

> Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
> Самое большое число-палиндром, полученное умножением двух двузначных чисел – `9009` = 91 × 99.
>
> Найдите самый большой палиндром, который меньше N и сделан из произведения двух 3-значных чисел.

``` python
solution(20000) # => 19591 = 143 x 137 
solution(30000) # => 29992 = 282 x 106
solution(40000) # => 39893 = 393 x 101
```
## Решение (1)

1. Начиная от числа N ищем число-полиндром 
2. Ищем два 3-значных делителей для полученного числа

``` python
def solution(n):
    for number in range(n - 1, 10000, -1):
        strNumber = str(number)
        if strNumber == strNumber[::-1]:
            divisor = 999
            while divisor != 99:
                if (number % divisor == 0) and (len(str(int(number / divisor))) == 3):
                    return number
                divisor -= 1
    return 'Palindrome not found'
```

Определить палиндром без использования строк можно так:

``` python
def is_palindromic(number: int) -> bool:
    reverse = 0
    i = number
    while i > 0:
        reverse = reverse * 10 + i % 10
        i //= 10
    return reverse == number
```
## Похожая задача:
> Найдите самый большой палиндром, сделаный из произведения двух n-значных чисел.

```python
def largestPalindromeProduct(n):
    largestNumber = int("9" * n)
    smallestNumber = int("1" + "0" * (n - 1))

    for i in range(largestNumber * largestNumber, smallestNumber * smallestNumber, -1):
        candidate = str(i)
        if candidate == candidate[::-1]:
            for j in range(largestNumber, smallestNumber, -1):
                if (j * j < i):
                    break  # если J^2 меньше палиндрома, то проверять меньшие значения j бесполезно
                for k in range(j, smallestNumber, -1):
                    if (j * k == i):
                        return i
                    elif (j * k < i):
                        break  # если произведение  меньше, то проверять меньшие значения k бесполезно
    return 'Palindrome not found'
```
```text
  №       Время  Замедление      Число    Результат
---  ----------  ------------  -------  -----------
  1   0.000237   0.024%              2         9009
  2   0.0345041  3.43%               3       906609
  3   0.301147   26.66%              4     99000099
  4  12.0154     1171.43%            5   9966006699
```