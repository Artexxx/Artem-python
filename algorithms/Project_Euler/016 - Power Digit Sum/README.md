# [Сумма цифр степени](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/16.html)


> `2^15` = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
>
>Какова сумма цифр числа `2^power`?


``` python
solution   (15)  # => 26 = 3 + 2 + 7 + 6 + 8 
solution   (20)  # => 31 = 1 + 0 + 4 + 8 + 5 + 7 + 6
solution   (50)  # => 76
```

## Частное решение (1)

```python

def solution(power):
    num = 2 ** power
    string_num = str(num)
    list_num = list(string_num)
    sum_of_num = 0

    for i in list_num:
        sum_of_num += int(i)
    return sum_of_num


def solution2(power):
    """Аналогичное решение без использования строк"""
    num = 2 ** power
    result_num = 0
    while num:
        result_num, num = result_num + num % 10, num // 10
    return result_num

solution3 = lambda n: sum(map(int, str(2 ** n)))
```

