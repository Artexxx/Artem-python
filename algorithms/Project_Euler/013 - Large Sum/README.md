# [Большая сумма](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/13.html)

>Найдите первые десять цифр суммы следующих ста 50-значных чисел.
>
> [37107287533902....](num.txt)

``` python
solution () # => 5_537_376_230
```

## Частное решение (1)

```python
solution = lambda array: str(sum(array))[:10]
```
```python
def solution2(int_numbers: list) -> int:
    """Аналогичное решение без использования строк"""
    all_sum = sum(int_numbers)
    DIGITS_LENGTH = 10
    while all_sum >= (10 ** DIGITS_LENGTH):
        all_sum //= 10
    return all_sum
```

## Общее решение (2)

```text
  ¹
  27
+ 59
----
  86
```

`7 + 9 = 16`, и цифра `1` является значением ***переноса***.

![image](https://user-images.githubusercontent.com/54672403/90874967-189ad580-e3a9-11ea-9b92-9cbf27317b2f.png)


```python
def compute_digit_and_carry(digits):
    """
    >>> compute_digit_and_carry([120, 7])
    digit, carry = (7, 12)
    """
    s = sum(digits)
    return s % 10, s // 10


def get_numbers_digit(numbers, ith):
    """
    >>> get_numbers_digit([[1, 2, 3],
    ...                    [4, 5, 6],
    ...                    [7, 8, 9]], 0)
    digits = [1, 4, 7]
    """
    return [int(r[ith]) for r in numbers]


def solve(numbers: List[str], first_n_digits) -> str:
    digit_number = len(numbers[0])
    carry = 0
    digits = []
    for c in range(digit_number - 1, -1, -1):
        d, carry = compute_digit_and_carry(get_numbers_digit(numbers, c) + [carry])
        digits.insert(0, d)
    digits = list(str(carry)) + digits
    return ''.join(map(str, digits[:first_n_digits]))
```
