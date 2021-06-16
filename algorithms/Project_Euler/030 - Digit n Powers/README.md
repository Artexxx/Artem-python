# [Пятые степени цифр](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/30.html)

> Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:
>
>1634 = 1<sup>4</sup> + 6<sup>4</sup> + 3<sup>4</sup> + 4<sup>4</sup><br>
8208 = 8<sup>4</sup> + 2<sup>4</sup> + 0<sup>4</sup> + 8<sup>4</sup><br>
9474 = 9<sup>4</sup> + 4<sup>4</sup> + 7<sup>4</sup> + 4<sup>4</sup>
>
>Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.
>
>Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.


``` python
solution   (4)  # => 19316 = 1634, 8208, 9474
solution   (5)  # => 443839 = 4150,4151,54748,92727,93084,194979
```



## Частное решение (1)

Теперь очень важно найти диапазон, из которого мы должны тестировать числа.

<br>Максимальное число n, для которого мы можем получить n-значное число с суммой пятой степени, равно 6.
<br>Потому что: 
```python
6*(9)^5 = 354294
```
Если взять n = 7:
```python
7*(9)^5 = 413343
```
Число по-прежнему состоит из 6 цифр.

Итак, верхняя граница равна `354294`

```python
def sum_digit_power(number) -> int:
    """
    Возвращает суммы пятых степеней цифр числа `number`:

    >>> digit_sum('4151')
    4151 #=> sum(1024, 1, 3125, 1)
    """
    return sum(pow(int(d), 5) for d in str(number))


def solution():
    return sum(i for i in range(1000, 6*(9)**5) if digit_power(i) == i)
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1      1.439  143,9%              5       443839 #  5083422 function calls
```

## Идея (2)

В приведенной выше постановке задачи в качестве первого примера, удовлетворяющего требованию суммирования степеней,
было использовано `1634`. Становится очевидным, что различные комбинации `1634` (1643, 1346, 1364, 1436, 1463, 3146, 3164, 3416, 3461, 3614, 3641, 4136, 4163, 4316, 4361, 4613, 4631, 6134, 6143, 6314, 6341, 6413, 6431)
будут иметь одну и ту же сумму степенных цифр.

**Пример:** возьмём произвольное число из приведенного выше набора, скажем `3614`, и посчитаем сумму 4-х степеней его цифр.
Сумма равна `1634`, как и для любой перестановки этого числа в наборе. 

## Улучшенное решение (2)

__Использование комбинаций__

```python
from itertools import combinations_with_replacement


def solution():
    result_sum = 0
    powers = {str(d): d ** 5 for d in range(10)}

    for digits in combinations_with_replacement('0123456789', 6):
        candidate = sum(powers[d] for d in digits)
        check_sum = sum(powers[d] for d in str(candidate))
        if candidate == check_sum:
            result_sum += candidate

    return result_sum - 1 # As 1 = 1^4 is not a sum it is not included.
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1      0.018  1.79%              5       443839 #  75762 function calls
```

<table>
<tbody><tr>
<th><ya-tr-span data-index="32-0" data-value="Power" data-translation="Сила" data-type="trSpan">Power</ya-tr-span><p></p>
</th><th><ya-tr-span data-index="33-0" data-value="Number Set" data-translation="Набор Чисел" data-type="trSpan">Number Set</ya-tr-span></th></tr>
<tr>
<td>2<p></p>
</td><td><ya-tr-span data-index="34-0" data-value="*NONE*" data-translation="*НИКТО*" data-type="trSpan">*NONE*</ya-tr-span></td></tr>
<tr>
<td>3<p></p>
</td><td>153, 370, 371, 407</td></tr>
<tr>
<td>4<p></p>
</td><td>1634, 8208, 9474</td></tr>
<tr>
<td>5<p></p>
</td><td>4150, 4151, 54748, 92727, 93084, 194979</td></tr>
<tr>
<td>6<p></p>
</td><td>548834</td></tr>
<tr>
<td>7<p></p>
</td><td>1741725, 4210818, 9800817, 9926315, 14459929</td></tr>
<tr>
<td>8<p></p>
</td><td>24678050, 24678051, 88593477</td></tr>
<tr>
<td>9<p></p>
</td><td>146511208, 472335975, 534494836, 912985153</td></tr>
<tr>
<td>10<p></p>
</td><td>4679307774</td></tr>
<tr>
<td>11<p></p>
</td><td>32164049650, 40028394225, 42678290603, 44708635679, 49388550606, 32164049651, 82693916578, 94204591914</td></tr>
<tr>
<td>12<p></p>
</td><td><ya-tr-span data-index="35-0" data-value="*NONE*" data-translation="*НИКТО*" data-type="trSpan">*NONE*</ya-tr-span></td></tr>
<tr>
<td>13<p></p>
</td><td>564240140138</td></tr>
<tr>
<td>14<p></p>
</td><td>28116440335967</td></tr>
<tr>
<td>15<p></p>
</td><td><ya-tr-span data-index="36-0" data-value="*NONE*" data-translation="*НИКТО*" data-type="trSpan">*NONE*</ya-tr-span></td></tr>
<tr>
<td>16<p></p>
</td><td>4338281769391370, 4338281769391371</td></tr>
<tr>
<td>17<p></p>
</td><td>233411150132317, 21897142587612075, 35641594208964132, 35875699062250035 </td></tr>
<tr>
<td>18<p></p>
</td><td><ya-tr-span data-index="37-0" data-value="*NONE*" data-translation="*НИКТО*" data-type="trSpan">*NONE*</ya-tr-span></td></tr>
<tr>
<td>19<p></p>
</td><td>1517841543307505039, 3289582984443187032, 4498128791164624869, 4929273885928088826</td></tr>
<tr>
<td>20<p></p>
</td><td>63105425988599693916</td></tr>
</tbody></table>