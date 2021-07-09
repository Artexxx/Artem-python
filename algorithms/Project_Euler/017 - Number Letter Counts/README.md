# [Счет букв в числительных](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/16.html)

>Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
>
>Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
>
>**Примечание**: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв.
><br> Использование "and" при записи чисел соответствует правилам британского английского.

``` python
solution   (5)  # => 19 = 3 + 3 + 5 + 4 + 4
solution   (1000)  # => 21124 
```

## Частное решение (1)
```python
import inflect
p = inflect.engine()

print(sum(len(p.number_to_words(n).replace('-', '').replace(' ', '')) for n in range(1, 1001)))
```

## Частное решение (2)

- Числа от 0 до 19 записываются в одно слово:
        zero, one, two, three, ... eighteen, nineteen

- Десятки (числа от 20 до 99 кратные 10) образуются с помощью числительного суффикса -ty и записываются также одно слово:
   twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
[#] Примечание: если последние цифра не равна 0, то мы дописываем two, three, four etc.
   twenty three, twenty four, twenty five ... ninety nine

- Сотни (числа от 200-900 кратные 100) образуются так: перед hundred ставим two, three, four etc.
   one hundred, two hundred, three hundred, ..., eight hundred, nine hundred
[#] Примечание: если последние две цифры не 00, то мы пишем слово "and"
    one hundred and one, one hundred and twenty three ... nine hundred and ninety nine

- Тысячи (числа от 1000 до 999999 кратные 1000) образуются так: перед thousand ставим two, three, four и переходим к сотням
    one thousand ten, one thousand one hundred, two thousand three hundred and forty five

```python
ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def convert_numbers_to_words(n) -> str:
    """
    params: n [int] - число, которое преобразуется в слово
    FIXME: Работает только с числами до миллиона
    """
    if 0 <= n < 20:
        return ONES[n]
    elif 20 <= n < 100:
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ONES[n // 100] + "hundred" + (("and" + convert_numbers_to_words(n % 100)) if (n % 100 != 0) else "")
    elif 1000 <= n < 1000000:
        return convert_numbers_to_words(n // 1000) + "thousand" + (convert_numbers_to_words(n % 1000) if (n % 1000 != 0) else "")
    else:
        raise ValueError(f"Число {n=} больше миллиона")


def solution(n):
    """Возвращает количество букв, используемых для записи всех чисел от 1 до n.
    [*] где n меньше или равно 999999.

    >>> solution(1000)
    21124
    >>> solution(5)
    19
    """
    return sum(len(convert_numbers_to_words(i)) for i in range(1, n+1))
```


```python
def solution(n):
    # zero, one, two, ..., nineteen
    ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    # twenty, thirty, ..., ninety
    tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

    count = 0
    for i in range(1, n + 1):
        if i < 1000:
            if i >= 100:
                # add number of letters for "n hundred"
                count += ones_counts[i // 100] + 7

                if i % 100 != 0:
                    # add number of letters for "and" if number is not multiple of 100
                    count += 3

            if 0 < i % 100 < 20:
                # add number of letters for one, two, three, ..., nineteen
                # (could be combined with below if not for inconsistency in teens)
                count += ones_counts[i % 100]
            else:
                # add number of letters for twenty, twenty one, ..., ninety nine
                count += ones_counts[i % 10]
                count += tens_counts[(i % 100 - i % 10) // 10]
        else:
            count += ones_counts[i // 1000] + 8
    return count
```
*[-] где `n` меньше или равно 1000*

