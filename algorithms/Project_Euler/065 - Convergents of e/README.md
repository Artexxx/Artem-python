# [Приближения e](TODO)
## [Проблема](https://euler.jakumo.org/problems/view/65.html)

>Квадратный корень из 2 можно записать в виде бесконечной непрерывной дроби.
> 
> <table border="0" cellspacing="0" cellpadding="0"><tbody>
> <tr>
> <td>√2 = 1 +</td>
> <td colspan="4"><div>1</div></td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>2 +</td>
> <td colspan="3"><div>1</div></td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>2 +</td>
> <td colspan="2"><div>1</div></td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>2 +</td>
> <td><div>1</div></td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>2 + ...</td>
> </tr>
> </tbody></table>
> 
> 
> Бесконечную непрерывную дробь можно записать, воспользовавшись обозначением √2 = [1;(2)], где (2) указывает на то, что 2 повторяется до бесконечности.
> Подобным образом, √23 = [4;(1,3,1,8)].
> 
> Оказывается, что последовательность частичных значений непрерывных дробей предоставляет наилучшую рациональную аппроксимацию квадратного корня.
> Рассмотрим приближения √2.
> 
>   <table border="0" cellspacing="0" cellpadding="0"><tbody>
> <tr>
> <td>1 +</td>
> <td><div>1</div></td>
> <td>= 3/2</td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td><div>2</div></td>
> <td>&nbsp;</td>
> </tr>
> </tbody></table>
> 
> <table border="0" cellspacing="0" cellpadding="0"><tbody>
> <tr>
> <td>1 +</td>
> <td colspan="2"><div>1</div></td>
> <td>= 7/5</td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>2 +</td>
> <td><div>1</div></td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td><div>2</div></td>
> <td>&nbsp;</td>
> </tr>
> </tbody></table>
> 
> <table border="0" cellspacing="0" cellpadding="0"><tbody>
> <tr>
> <td>1 +</td>
> <td colspan="3"><div>1</div></td>
> <td>= 17/12</td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>2 +</td>
> <td colspan="2"><div>1</div></td>
> <td>&nbsp;</td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>2 +</td>
> <td><div>1</div></td>
> <td>&nbsp;</td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td><div>2</div></td>
> <td>&nbsp;</td>
> </tr>
> </tbody></table>
> 
> <table border="0" cellspacing="0" cellpadding="0"><tbody>
> <tr>
> <td>1 +</td>
> <td colspan="4"><div>1</div></td>
> <td>= 41/29</td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>2 +</td>
> <td colspan="3"><div>1</div></td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>2 +</td>
> <td colspan="2"><div>1</div></td>
> <td>&nbsp;</td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>2 +</td>
> <td><div>1</div></td>
> <td>&nbsp;</td>
> </tr>
> <tr>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td>&nbsp;</td>
> <td><div>2</div></td>
> <td>&nbsp;</td>
> </tr>
> </tbody></table>
> 
> 
> Таким образом, последовательность первых десяти приближений для √2 имеет вид:
> 
>     1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
> 
> Самое удивительное, что важная математическая константа
> 
>     e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
> 
> Первые десять членов последовательности приближений для e перечислены ниже:
> 
>     2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
> 
> Сумма цифр числителя 10-го приближения равна 1 + 4 + 5 + 7 = 17.
> 
> Найдите сумму цифр числителя 100-го приближения непрерывной дроби для e.

``` python
solution (100) => 272 
```

## Частное решение (1)

|   k   | numerator | continuous fraction |
|----   |   ----     | ---------          |
|   1   |      2    |          1          |
|   2   |      3    |          2          |
|   3   |      8    |          1          |
|   4   |     11    |          1          |
|   5   |     19    |          4          |
|   6   |     87    |          1          |
|   7   |    106    |          1          |
|   8   |    193    |          6          |
|   9   |   1264    |          1          |
|  10   |   1457    |          1          |

Посмотрев первые 10 числителей, несложно уловить закономерность:
numerator(i) = numerator(i-2) + numerator(i-1) * fraction(i-1)

**Примечание**: Числители растут довольно быстро.
К примеру, числитель для "k=100" содержит 58 десятичных цифр.

```python
def solution(N):
    last_three_numerators = deque([2, 3], maxlen=2)

    for index in range(3, N+1):
        fraction_number = 1
        if index % 3 == 0:
            fraction_number = (index // 3) * 2

        new_numerator = last_three_numerators[0] + last_three_numerators[1] * fraction_number
        last_three_numerators.append(new_numerator)

    return sum(map(int, str(last_three_numerators[-1])))
```
```text
  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  6.37e-05   0.006%               100          272 (Ответ)
  2  0.0006653  0.060%              1000         4034
  3  0.0195435  1.888%             10000        55322
```
