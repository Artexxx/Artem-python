# [Сумма последовательных простых чисел](TODO)
## [Проблема](https://euler.jakumo.org/problems/view/51.html)

>Меняя первую цифру числа *3 (двузначного числа, заканчивающегося цифрой 3),
> оказывается, что шесть из девяти возможных значений - 13, 23, 43, 53, 73 и 83 - являются простыми числами.
>
>При замене третьей и четвертой цифры числа 56**3 одинаковыми цифрами, получаются десять чисел,
> из которых семь - простые: 56003, 56113, 56333, 56443, 56663, 56773 и 56993.
>
>Число 56**3 является наименьшим числом, подставление цифр в которое дает именно семь простых чисел.
>
>Соответственно, число 56003, будучи первым из полученных простых чисел, является наименьшим простым числом, обладающим указанным свойством.
>
>Найдите наименьшее простое число, которое является одним из восьми простых чисел, полученных заменой части цифр (не обязательно соседних) одинаковыми цифрами.

                   

``` python
solution  () => 121313
```

## Нормальное решение (1)

```python
def count_duplicated_digits(number: int) -> int:
    return len(str(number)) - len(set(str(number)))


def get_duplicated_digits(number: str) -> str:
    """ Возвращает повторяющиеся цифры
    >>> list(get_duplicated_digits("1122334"))
    ['1', '2', '3']
    """
    for digit, count in Counter(number).items():
        if count > 1:
            yield digit


def get_patterns(number: int) -> str:
    """ Возвращает паттерны повторяющихся цифр
    >>> list(get_patterns(1122334))
    ['**22334', '11**334', '1122**4']
    """
    number = str(number)
    for digit in get_duplicated_digits(number):
        yield number.replace(digit, "*")


def get_candidates(pattern):
    for digit in digits:
        yield int(pattern.replace("*", digit))


def solution():
    """
    Находит наименьшее простое число, которое является одним из восьми простых чисел, полученных заменой части цифр (не обязательно соседних) одинаковыми цифрами.
    """
    primes = [prime for prime in prime_sieve(10 ** 6) if count_duplicated_digits(prime) >= 3]

    patterns_view = []
    for prime in primes:

        for pattern in get_patterns(prime):
            if pattern in patterns_view:
                continue
            else:
                primes_count = 0

                for candidate in get_candidates(pattern):
                    if candidate in primes and (len(str(candidate)) == len(str(prime))):
                        primes_count += 1
                if primes_count == 8:
                    return prime
                patterns_view.append(pattern)
```
```text
   Время  Замедление    Аргумент      Результат
--------  ------------  ----------  ----------- <333732 function calls>
0.317896  31.790%                        121313 (Ответ)
```

