# [Треугольные, пятиугольные и шестиугольные](TODO)

                   
## [Проблема](https://euler.jakumo.org/problems/view/45.html)


>Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:
>
>Треугольные	T(n) = n(n+1)/2 	1, 3, 6, 10, 15, ...
>
>Пятиугольные	P(n) = n(3n-1)/2 	1, 5, 12, 22, 35, ...
>
>Шестиугольные	H(n) = n(2n-1) 	 	1, 6, 15, 28, 45, ...
>
>Можно убедиться в том, что T( 285 ) = P( 165 ) = H( 143 ) = 40755.
>
>
> Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным.
                                        
``` python
solution  () => 1533776805
```

## Частное решение (1)


```python
def generate_polygonal(type_number):
    """Генерирует фиругные числа

    >>> generate_polygonal(type_number=3)
    1 3 6 10 15 21 28 36
    >>> generate_polygonal(type_number=4)
    1 4 9 16 25 36 49 64
    """
    c = type_number - 2
    a = b = 1
    while True:
        yield a
        b += c
        a += b


def is_triangle(num):
    n = ((1 + 8 * num) ** 0.5 - 1) / 2
    return n.is_integer()


def solution(start_number=40755):
    """
    Возращает следующее треугольное число, являющееся также пятиугольным и шестиугольным.

    >>> solution()
    1533776805
    """

    hexagonal = generate_polygonal(type_number=6)
    pentagonal = generate_polygonal(type_number=5)
    h = next(hexagonal)
    p = next(pentagonal)

    while True:
        while p < h:
            p = next(pentagonal)
        if p == h and p > start_number and is_triangle(p) :
            return p
        h = next(hexagonal)
```
```text
    Время  Замедление         Число       Результат
---------  ------------  ----------  --------------
5.28e-05   0.005%                 1           40755
0.0097281  0.968%             40755      1533776805 (Ответ)
1.92689    191.716%      1533776805  57722156241751
```


##  Идея (2)

![Треугольник паскаля c foxford](https://user-images.githubusercontent.com/54672403/123087190-ef196300-d42c-11eb-9a3f-a5ecba3a2017.jpg)
Одно из свойств треугольника Паскаля:
<br>
Вдоль диагоналей, параллельных сторонам треугольника, выстроены треугольные числа, тетраэдрические числа и т.д.
