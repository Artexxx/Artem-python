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

```python
ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def to_english(n):
    """
    - For the numbers 0 to 19, we write the single word:
      {zero, one, two, three, four, five, six, seven, eight, nine,
      ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen}.
    - For the numbers 20 to 99, we write the word for the tens place:
      {twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety}.
      Subsequently if the last digit is not 0, then we write the word for the ones place (one to nine).
    - For the numbers 100 to 999, we write the ones word for the hundreds place followed by "hundred":
      {one hundred, two hundred, three hundred, ..., eight hundred, nine hundred}.
      Subsequently if the last two digits are not 00, then we write the word "and"
      followed by the phrase for the last two digits (from 01 to 99).
    - For the numbers 1000 to 999999, we write the word for the three digits starting at the
      thousands place and going leftward, followed by "thousand". Subsequently if the last three
      digits are not 000, then we write the phrase for the last three digits (from 001 to 999).
    """
    if 0 <= n < 20:
        return ONES[n]
    elif 20 <= n < 100:
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ONES[n // 100] + "hundred" + (("and" + to_english(n % 100)) if (n % 100 != 0) else "")
    elif 1000 <= n < 1000000:
        return to_english(n // 1000) + "thousand" + (to_english(n % 1000) if (n % 1000 != 0) else "")
    else:
        raise ValueError()


def solution(n):
    return sum(len(to_english(i)) for i in range(1, n+1))


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

