# [Су Доку](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/96.html)

> <p>Су Доку (по-японски значит <i>место числа</i>) - название популярной головоломки. Ее происхождление неизвестно, однако нужно отдать должное Леонарду Эйлеру, который придумал идею похожей, но более сложной головоломки под названием Латинские Квадраты. Целью Су Доку является заменить пустые места (или нули) в сетке 9 x 9 цифрами таким образом, чтобы в каждой строке, колонке и квадрате 3 x 3 содержались все цифры от 1 до 9. Ниже приведен пример типичной исходной головоломки и ее решение.</p>
>
>
<div style="text-align:center;">
<table align="center" border="0" cellpadding="0" cellspacing="0"><tbody><tr><td>
<table border="1" cellpadding="5" cellspacing="0"><tbody><tr><td style="font-family:'courier new';font-size:14pt;">0 0 3<br>9 0 0<br>0 0 1<br></td>
<td style="font-family:'courier new';font-size:14pt;">0 2 0<br>3 0 5<br>8 0 6</td>
<td style="font-family:'courier new';font-size:14pt;">6 0 0<br>0 0 1<br>4 0 0</td>
</tr><tr><td style="font-family:'courier new';font-size:14pt;">0 0 8<br>7 0 0<br>0 0 6</td>
<td style="font-family:'courier new';font-size:14pt;">1 0 2<br>0 0 0<br>7 0 8</td>
<td style="font-family:'courier new';font-size:14pt;">9 0 0<br>0 0 8<br>2 0 0</td>
</tr><tr><td style="font-family:'courier new';font-size:14pt;">0 0 2<br>8 0 0<br>0 0 5</td>
<td style="font-family:'courier new';font-size:14pt;">6 0 9<br>2 0 3<br>0 1 0</td>
<td style="font-family:'courier new';font-size:14pt;">5 0 0<br>0 0 9<br>3 0 0</td>
</tr></tbody></table></td>
<td width="50"><img alt="" height="1" src="images/spacer.gif" width="50"><br></td>
<td>
<table border="1" cellpadding="5" cellspacing="0"><tbody><tr><td style="font-family:'courier new';font-size:14pt;">4 8 3<br>9 6 7<br>2 5 1</td>
<td style="font-family:'courier new';font-size:14pt;">9 2 1<br>3 4 5<br>8 7 6</td>
<td style="font-family:'courier new';font-size:14pt;">6 5 7<br>8 2 1<br>4 9 3</td>
</tr><tr><td style="font-family:'courier new';font-size:14pt;">5 4 8<br>7 2 9<br>1 3 6</td>
<td style="font-family:'courier new';font-size:14pt;">1 3 2<br>5 6 4<br>7 9 8</td>
<td style="font-family:'courier new';font-size:14pt;">9 7 6<br>1 3 8<br>2 4 5</td>
</tr><tr><td style="font-family:'courier new';font-size:14pt;">3 7 2<br>8 1 4<br>6 9 5</td>
<td style="font-family:'courier new';font-size:14pt;">6 8 9<br>2 5 3<br>4 1 7</td>
<td style="font-family:'courier new';font-size:14pt;">5 1 4<br>7 6 9<br>3 8 2</td>
</tr></tbody></table></td>
</tr></tbody></table></div>

>Правильно составленная головоломка Су Доку имеет единственное решение и может быть решена с помощью логики, однако иногда необходимо применять метод "гадай и проверяй", чтобы исключить неверные варианты (существует очень спорное мнение по этому поводу). Сложность поиска определяет уровень головоломки. Приведенный выше пример считается <i>легким</i>, так как его можно решить прямой дедукцией.
>
>Решите все пятьдесят головоломок, найдите сумму трехзначных чисел, находящихся в верхнем левом углу каждого решения. Например, 483 является трехзначным числом, находящимся в верхнем левом углу приведенного выше решения.


``` python
solution  (500)  # => 24702
```


## Читерское решение (1)

```python
from dlxsudoku.sudoku import Sudoku

s = [l for l in open('p096_sudoku.txt').readlines() if l[0].isdigit()]
sudokus = [Sudoku(''.join(s[i * 9:(i + 1) * 9])) for i in range(50)]

for sudoku in sudokus: sudoku.solve()

result = sum(int(sudoku.to_oneliner()[:3]) for sudoku in sudokus)
print(result)
```
```text
  №      Время  Замедление   Количество    Результат
---  ---------  -----------  ----------  -----------
  1      0.274  0,027%        500         24702
```

## Медленное решение (1)

```
Ищем пустую клетку и находим для неё число {1-9} |
    - проверяем ошибку по строкам и столбцам     |> <повтор если всё хорошо>
    |> стираем значение и возращаемся на два шага назад
```        
```python
def find_empty(bo):
    """
    :return координаты пустой ячейки (строка, столбец)
    - пустая ячейка заполненая 0
    """
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return i, j


def valid(bo, num, pos):
    """
    Проверяет пригодность числа для пустой ячейки
    :param bo таблица с судоку
    :param num {1-9} число для проверки
    :param pos (строка, столбец) позиция числа
    :return bool
    """
    # Проверка строки
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Проверка столбца
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Проверка квадрата
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(bo):
    global tries
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            tries += 1
            if solve(bo):
                return True
            bo[row][col] = 0
    return False
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1   0.327112  32.711%             5         1850
  2   3.90085   357.37%            10         4231
  3  18.5256    1462.47%           50        24702
```