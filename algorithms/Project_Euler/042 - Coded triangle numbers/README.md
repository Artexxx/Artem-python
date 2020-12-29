# [Закодированные треугольные числа](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/42.html)

>n-ый член последовательности треугольных чисел задается как t_n = 1/2 n (n+1). 
>
>Таким образом, первые десять треугольных чисел:
>
>1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
>
>Преобразовывая каждую букву в число, соответствующее ее порядковому номеру в алфавите, и складывая эти значения, мы получим числовое значение слова.
> Для примера, числовое значение слова SKY равно 19 + 11 + 25 = 55 = t_10.
> Если числовое значение слова является треугольным числом, то мы назовем это слово треугольным словом.
>
>Используя words.txt текстовый файл, содержащий около двух тысяч часто используемых английских слов, определите, сколько в нем треугольных слов.


``` python
solution  () => 162
```

## Частное решение (1)

Т.к в английском алфавмте всего 26 букв, то треугольных чисел больше 26 не нужно.

```python
triangleNumbers = [0.5 * n * (n + 1)
                   for n in range(30)]


def word_value(word):
    return sum(ord(char) - ord('A') + 1 
               for char in word)


def solution(words: list):
    return sum(1
               for word in words
               if word_value(word) in triangleNumbers)
```

## Математическое решение (1)


__Идея:__ Если вывести формулу треугольниного числа от n, то мы можем проверять числа на то, что они являются треугольными.
 
<img src="https://user-images.githubusercontent.com/54672403/99879116-9fb35000-2c1b-11eb-935f-3e44d5a5b912.jpg">


 Поскольку это квадратное уравнение, мы будем использовать квадратную формулу для решения для n.

Квадратичная формула: <img src="https://user-images.githubusercontent.com/54672403/99879177-1f411f00-2c1c-11eb-9d71-6f3770a9551f.jpg">

Используя квадратичную формулу для решения от n с коэффициентами: `a = 1`, `b = 1` и `c = - 2t_n`

<img src="https://user-images.githubusercontent.com/54672403/99879115-9e822300-2c1b-11eb-8e34-50a638023e1f.jpg">

``` python
as_int = lambda n: n == int(n)

isTrNumber = lambda t: as_int((sqrt(1 + 8*t) - 1) / 2)


def word_value(word):
    return sum(ord(char) - ord('A') + 1
               for char in word)


def solution(words: list):
    """
    Возращает количество треугольных слов
    >>> solution()
    ... 162
    """
    return sum(1
               for word in words
               if isTrNumber(word_value(word)))
```