# [Очки за имена](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/22.html)

> Используя массив имён, содержащий более пяти тысяч имен, начните с сортировки в алфавитном порядке. 
>Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.
>
> Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-ым в списке. 
>Поэтому, имя COLIN получает 938 × 53 = 49714 очков.
>
>Какова сумма очков имен в файле?

``` python
solution   ()  # => 871_198_282
```

## Частное решение (1)

- ord("A") # => 65 = 64 + 1
- ord("Z") # => 90 = 64 + 26
```python
def solution(n):
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
        names = str(file.readlines()[0]).split(",")
    names.sort()

    name_score = 0
    total_score = 0
    for i, name in enumerate(names):
        for letter in name:
            name_score += ord(letter) - 64

        total_score += (i + 1) * name_score
        name_score = 0
    return total_score
```

## Частное решение (2)

- ord("A") # => 65 = 64 + 1
- ord("Z") # => 90 = 64 + 26
```python
def letter_index_upper(letter) -> int:
    """Возвращает алфавитный индекс заглавной буквы.
     'A' -> 1, 'Z' -> 26.
    """
    return ord(letter) - ord('A') + 1


def name_score(name, position) -> int:
    """Возвращает оценку для имени в позиции при сортировке в алфавитном порядке."""

    score = sum(map(letter_index_upper, name))
    return position * score


def solution() -> int:
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file:
        names = str(file.readlines()[0]).split(",")
    heapq.heapify(names)  # сортировка

    total = 0
    for i in range(1, len(names) + 1):
        # heappop - Возвращает min элемент, удаляет его из кучи
        total += name_score(heapq.heappop(names), i)

    return total
```
```text
    Время  Замедление    Аргумент      Результат
---------  ------------  ----------  -----------
0.0084408  0.844%                      871190344 <108414 function calls>
```


