# [Наибольшее произведение в таблице](https://www.codewars.com/kata/58062572a4647eb3f50002e5/solutions)

## [Проблема](https://euler.jakumo.org/problems/view/11.html)

> В таблице 20×20 (внизу) четыре числа на одной диагонали выделены красным.
>
><p style="font-family:courier new;text-align:center;font-size:10pt;">
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08<br>
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00<br>
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65<br>
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91<br>
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80<br>
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50<br>
32 98 81 28 64 23 67 10 <span style="background:#ff0000;"><b>26</b></span> 38 40 67 59 54 70 66 18 38 64 70<br>
67 26 20 68 02 62 12 20 95 <span style="background:#ff0000;"><b>63</b></span> 94 39 63 08 40 91 66 49 94 21<br>
24 55 58 05 66 73 99 26 97 17 <span style="background:#ff0000;"><b>78</b></span> 78 96 83 14 88 34 89 63 72<br>
21 36 23 09 75 00 76 44 20 45 35 <span style="background:#ff0000;"><b>14</b></span> 00 61 33 97 34 31 33 95<br>
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92<br>
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57<br>
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58<br>
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40<br>
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66<br>
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69<br>
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36<br>
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16<br>
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54<br>
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48</p>
>
> Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20, расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали)?

``` python
solution (4) # => 70600674 = 26 * 63 * 78 * 14
```

## Частное решение (1)

```python
def largest_product(grid):
    nColumns = len(grid[0])
    nRows = len(grid)

    largest = 0
    lrDiagProduct = 0
    rlDiagProduct = 0

    # Проверка по вертикали, горизонтали, диагонали одновременно (работает только для квадратного массива n х n )
    for i in range(nColumns):
        for j in range(nRows - 3):
            vertProduct = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i]
            horzProduct = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]

            # Диагональ слева направо  (\)
            if i < nColumns - 3:
                lrDiagProduct = (
                        grid[i][j]
                        * grid[i + 1][j + 1]
                        * grid[i + 2][j + 2]
                        * grid[i + 3][j + 3]
                )
            # Диагональ справа налево (/)
            if i > 2:
                rlDiagProduct = (
                        grid[i][j]
                        * grid[i - 1][j + 1]
                        * grid[i - 2][j + 2]
                        * grid[i - 3][j + 3]
                )
            maxProduct = max(vertProduct, horzProduct, lrDiagProduct, rlDiagProduct)
            if maxProduct > largest:
                largest = maxProduct
    return largest
```
*[-] Работает только для квадратного массива `n х n`*


## Общее решение (1)

*[+] Работает для прямоугольного массива*
```python
def solution():
    ans = -1
    width = len(GRID[0])
    height = len(GRID)
    for y in range(height):
        for x in range(width):
            if x + CONSECUTIVE <= width:
                ans = max(grid_product(x, y, 1, 0, CONSECUTIVE), ans)
            if y + CONSECUTIVE <= height:
                ans = max(grid_product(x, y, 0, 1, CONSECUTIVE), ans)
            if x + CONSECUTIVE <= width and y + CONSECUTIVE <= height:
                ans = max(grid_product(x, y, 1, 1, CONSECUTIVE), ans)
            if x - CONSECUTIVE >= -1 and y + CONSECUTIVE <= height:
                ans = max(grid_product(x, y, -1, 1, CONSECUTIVE), ans)
    return str(ans)

def grid_product(ox, oy, dx, dy, n):
    """
[1, 2, 3, 0],
[4, 5, 6, 0],      CONSECUTIVE = 2
[7, 8, 9, 0],
[0, 0, 0, 0],

Будем начинать из (x, y) = (0, 0)

1. Горизонталь: Хочу получить произведение 1, 2, 3
>>> grid_product(x, y,  1, 0, CONSECUTIVE) # => 6

2. Вертикаль: Хочу получить произведение 1, 4, 7
>>> grid_product(x, y,  1, 0, CONSECUTIVE) # => 28

3.  Диагональ слева направо (\): Хочу получить произведение 1, 5, 9
>>> grid_product(x, y,  1, 1, CONSECUTIVE) # => 45

4. Для диагонали справа налево (/) буду начинать из (x, y) = (2, 0)
   Хочу получить произведение  3, 5, 7
>>> grid_product(x:=2, y:=0,  -1, 1, CONSECUTIVE) # => 105
"""
    result = 1
    for i in range(n):
        result *= GRID[oy + i * dy][ox + i * dx]
    return result
```
