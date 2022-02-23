# [Сумма цифр степени](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/16.html)


> `2^15` = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
>
>Какова сумма цифр числа `2^power`? `power` = 1000


``` python
solution   (15)  # => 26 = 3 + 2 + 7 + 6 + 8 
solution   (20)  # => 31 = 1 + 0 + 4 + 8 + 5 + 7 + 6
solution   (50)  # => 76
```

## Нормальные решения

```python
solution = lambda n: sum(map(int, str(2 ** n)))
```

Аналогичное решение без использования строк:
```python
def solution2(power):
    num = 2 ** power
    result_num = 0
    while num:
        result_num, num = result_num + num % 10, num // 10
    return result_num
```

```text
  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  2.84e-05   0.003%              1000         1366 (ответ)
  2  0.0003635  0.034%             10000        13561
  3  0.0141451  1.378%            100000       135178
```