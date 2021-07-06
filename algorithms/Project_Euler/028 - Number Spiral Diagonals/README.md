# [Диагонали числовой спирали](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/28.html)

> Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:
>
><p style="text-align:center;font-family:'courier new';"><span style="color:#ff0000;font-family:'courier new';"><b>21</b></span> 22 23 24 <span style="color:#ff0000;font-family:'courier new';"><b>25</b></span><br>
>20 &nbsp;<span style="color:#ff0000;font-family:'courier new';"><b>7</b></span> &nbsp;8 &nbsp;<span style="color:#ff0000;font-family:'courier new';"><b>9</b></span> 10<br>
>19 &nbsp;6 &nbsp;<span style="color:#ff0000;font-family:'courier new';"><b>1</b></span> &nbsp;2 11<br>
>18 &nbsp;<span style="color:#ff0000;font-family:'courier new';"><b>5</b></span> &nbsp;4 &nbsp;<span style="color:#ff0000;font-family:'courier new';"><b>3</b></span> 12<br><span style="color:#ff0000;font-family:'courier new';"><b>17</b></span> 16 15 14 <span style="color:#ff0000;font-family:'courier new';"><b>13</b></span></p>
>
>Можно убедиться, что сумма чисел в диагоналях равна `101`.
>
>Какова сумма чисел в диагоналях спирали `1001` на `1001`, образованной таким же способом?

``` python
solution   (5)  # => 101
solution   (50)  # => 79697
solution   (1001)  # => 669171001
```

## Примечание (1)

Рассмотрим спираль, приведенную в примере.

| digit | Index |
| ----- | ----- |
| 1     | 0     |
| 3     | 2     |
| 5     | 4     |
| 7     | 6     |
| 9     | 8     |
| 13    | 12    |
| 17    | 16    |
| 21    | 20    |
| 25    | 24    |

При прохлждении каждого квадрата индекс нужного числа увеличивается на 2, потом на 4, потом на 6..., до тех пор,
пока мы не достигнем цифры, завершающей сетку.


| digit | Index |
| ----- | ----- |
| 25    | 24    |
| 31    | 30    |
| 37    | 36    |
| 43    | 42    |
| 49    | 48    |


__Вывод формулы:__

Рассмотрим четыре угла квадрата `n * n`  в спирали  (где N нечетно).
Нетрудно убедить себя, что верхний правый угол всегда имеет значение `n^2`.
Работая против часовой стрелки (назад), верхний левый угол имеет значение `n^2 - (n-1)`,
нижний левый угол имеет значение `n^2-2(n-1)`, а нижний правый - `n^2 - 3(n-1)`.
Сложив все это вместе, это самое внешнее кольцо вносит вклад `4n^2-6 (n - 1)` в конечную сумму.

Кстати, замкнутая форма этой суммы равна `(4М^3 + 3м^2 + 8м-9) / 6`, где М = размер.
3 + 5 + 7 + 9 = **24**, 13 + 17 + 21 + 25 = **76**, 31 + 37 + 43 + 49 = **160**

Эти суммы углов образуют сумму диагоналей, после сложения `1` для центра, для каждой спирали `i` на `i`, где `3 ≤ i ≤ n`, для нечетного `n` и могут быть выражены как:
<br>
<img src="https://s0.wp.com/latex.php?latex=+1%2B%5Csum%5Climits_%7Bi%3D1%7D%5E%7Bs%7D+4%282i%2B1%29%5E2-6%282i%2B1%29%2B6%2C+s%3D%5Cfrac%7Bn-1%7D%7B2%7D+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt=" 1+\sum\limits_{i=1}^{s} 4(2i+1)^2-6(2i+1)+6, s=\frac{n-1}{2} " title=" 1+\sum\limits_{i=1}^{s} 4(2i+1)^2-6(2i+1)+6, s=\frac{n-1}{2} " class="latex">
<br>
и упрощен до:
<br>
<img src="https://s0.wp.com/latex.php?latex=+1%2B%5Csum%5Climits_%7Bi%3D1%7D%5E%7Bs%7D+16i%5E2%2B4i%2B4+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt=" 1+ \ sum\limits_{i=1}^{s} 16i^2+4i+4 " title=" 1+ \ sum\limits_{i=1}^{s} 16i^2+4i+4 " class="latex">
<br>
<br>
Наконец, мы можем еще больше упростить это суммирование:
<br>
<img src="https://s0.wp.com/latex.php?latex=+1%2B16%5Ccdot%5Csum%5Climits_%7Bi%3D1%7D%5E%7Bs%7Di%5E2+%2B+4%5Ccdot%5Csum%5Climits_%7Bi%3D1%7D%5E%7Bs%7Di+%2B+%5Csum%5Climits_%7Bi%3D1%7D%5E%7Bs%7D4+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt=" 1+16\cdot\sum\limits_{i=1}^{s}i^2 + 4\cdot\sum\limits_{i=1}^{s}i + \sum\limits_{i=1}^{s}4 " title=" 1+16\cdot\sum\limits_{i=1}^{s}i^2 + 4\cdot\sum\limits_{i=1}^{s}i + \sum\limits_{i=1}^{s}4 " class="latex">
<br>
<br>
<img src="https://s0.wp.com/latex.php?latex=+%5Cfrac%7B16s%28s+%2B+1%29%282s+%2B+1%29%7D%7B6%7D+%2B+%5Cfrac%7B4s%28s+%2B+1%29%7D%7B2%7D+%2B+4s+%2B+1+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt=" \frac{16s(s + 1) (2s + 1)}{6} + \frac{4s (s + 1)}{2} + 4s + 1 " title=" \frac{16s(s + 1) (2s + 1)}{6} + \frac{4s (s + 1)}{2} + 4s + 1 " class="latex">
<br>
<br>
<img src="https://s0.wp.com/latex.php?latex=+%5Cfrac%7B16s%5E3+%2B+30s%5E2+%2B+26s+%2B3%7D%7B3%7D+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt=" \frac{16s^3 + 30s^2 + 26s +3}{3} " title=" \frac{16s^3 + 30s^2 + 26s +3}{3} " class="latex">
<br>
<br>
<img src="https://s0.wp.com/latex.php?latex=+%28%5Cfrac%7B2s%7D%7B3%7D%29+%288s%5E2+%2B+15s+%2B+13%29+%2B+1+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt=" (\frac{2s}{3}) (8s^2 + 15s + 13) + 1 " title=" (\frac{2s}{3}) (8s^2 + 15s + 13) + 1 " class="latex">
<br>
<br>
Проверим это уравнение на примере в постановке задачи, `n` (нечетная длина стороны ≥ 3) = 5:  `s = \frac{5-1}{2} = 2`
<br>
<img src="https://s0.wp.com/latex.php?latex=+%5Cfrac%7B16%5Ccdot2%5E3+%2B+30%5Ccdot2%5E2+%2B+26%5Ccdot2+%2B3%7D%7B3%7D%3D+101+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt=" \frac{16\cdot2^3 + 30\cdot2^2 + 26\cdot2 +3}{3}= 101 " title=" \frac{16\cdot2^3 + 30\cdot2^2 + 26\cdot2 +3}{3}= 101 " class="latex">
 
## Частное решение (1)
- `n ** 2` - наибольшее число в спирали NxN

```python
def solution(n):
    result = 1
    number = 1
    step = 2
    while (number < n ** 2):
        for _ in range(4):
            number += step
            result += number
        step += 2
    return result
```

## Общее решение (1)

```python
def solution(n):
    s = (n - 1) // 2
    return (16 * s * s * s + 30 * s * s + 26 * s + 3) // 3
```
