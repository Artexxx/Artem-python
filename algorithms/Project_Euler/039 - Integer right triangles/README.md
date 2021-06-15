# [Целые прямоугольные треугольники](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/39.html)

>Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c}, то существует ровно три решения для p = 120:
>
>{20,48,52}, {24,45,51}, {30,40,50}
>
>Какое значение p ≤ 1000 дает максимальное число решений?

``` python
solution  ()  # => 840 # 16 решений

    Полученные решения:
     [40, 399, 401]
     [40, 399, 401]
     [56, 390, 394]
     [56, 390, 394]
          ...
     [210, 280, 350]
     [210, 280, 350]
     [240, 252, 348]
     [240, 252, 348]
```

## Частное решение (1)

[-] Считает одно и тоже решение сначало для `a`, а потом для `b`

```python
is_valid_sqrt = lambda n: n == int(n)
is_valid_triangle = lambda a, b, c: all((a, b, c))

def perimeters_generator():
    for a, b in product(range(500), range(500)):
        c: float = sqrt(a * a + b * b)
        if is_valid_sqrt(c) and a + b + c <= 1000 and is_valid_triangle(a, b, c):
            yield a + b + int(c)


def solution():
    """
    Возращает периметр, для которого существует максимальное число решений
    >>> solution()
    840 # 16 решений
    Полученные решения:
     [40, 399, 401]
     [40, 399, 401]
     [56, 390, 394]
     [56, 390, 394]
          ...
     [210, 280, 350]
     [210, 280, 350]
     [240, 252, 348]
     [240, 252, 348]
    """
    count_dict = dict()
    for p in perimeters_generator():
        if count_dict.get(p):
            count_dict[p] += 1
        else:
            count_dict[p] = 1
    return max(count_dict,  key=lambda x: count_dict[x])
```

## Нормальное решение (1)

Мы знаем, что p = a + b + c
 
1. если `a` и `b` будут чётными, то `c` будет чётным, периметр чётный 
2. если `a` или `b` будут нечётными, то `c` тоже будет нечётным, периметр чётный
3. если `a` и `b` будут нечётными, то `c`  будет чётным, периметр чётный

Из `1`, `2`, `3` следует, что периметр всегда чётный

Мы знаем, что `c=p-a-b`.

<img src='https://user-images.githubusercontent.com/54672403/98253143-bc008d00-1f8b-11eb-9a53-469f5fcce298.jpg' width=600px>



Вывод формулы для `b`:

<img src='https://user-images.githubusercontent.com/54672403/98253344-f5d19380-1f8b-11eb-8ac6-47a7c7cd5ef8.jpg' width=200px>

Анализ полученной формулы:
1. Если `b` является целым числом, то  треугольник с параметрами `a` и `p` существует.


```python
def solution(LIMIT=1000):
    """
    Возращает периметр, для которого существует максимальное число решений
    >>> solution()
    840 # 9 решений
    """
    result_perimeter = None
    max_count = 0

    for p in range(2, LIMIT, 2):
        count_solutions = 0
        for a in range(2, int(p / 3)):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                count_solutions += 1
        if count_solutions > max_count:
            max_count = count_solutions
            result_perimeter = p
    return result_perimeter
```

**Примечание:**

`a<p/3`, т.к `a<c` и `b<c`, следовательно `a≤b` 
