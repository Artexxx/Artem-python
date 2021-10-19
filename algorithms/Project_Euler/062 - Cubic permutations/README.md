# [Кубические перестановки](TODO)
## [Проблема](https://euler.jakumo.org/problems/view/61.html)

>Можно найти перестановки куба 41063625 (345<sup>3</sup>), чтобы получить еще два куба: 56623104 (384<sup>3</sup>) и 66430125 (405<sup>3</sup>). К слову, 41063625 является наименьшим кубом, для которого ровно три перестановки также являются кубами
>
>Найдите наименьший куб, для которого ровно пять перестановок также являются кубами.
``` python
solution (5) => 127035954683
```

## Частное решение (1)
```python
def solution(N):
    sorted_cubes = {}

    for x in itertools.count(1):
        cube = pow(x, 3)
        cube_digits = ''.join(sorted(str(cube)))
        cached_cube = sorted_cubes.get(cube_digits)

        if cached_cube is not None:
            cached_cube['count'] += 1
            cached_cube['cubes'].append(cube)

            if cached_cube['count'] == N:
                return min(cached_cube['cubes'])
        else:
            sorted_cubes[cube_digits] = {'count': 1, 'cubes': [cube]}
```
```text
  №      Время  Замедление      Аргумент          Результат
---  ---------  ------------  ----------  -----------------
  1  0.0291759  2.918%                 5       127035954683
  2  0.149325   12.015%               10    126120833457949
  3  1.07143    92.210%               30  11237467249565803
```
## Частное решение (2)
Оптимизированная версия первого решения с помощью `defaultdict`.
```python
def solution(N):
    mapping = defaultdict(int)
    mapping_sequence = defaultdict(list)

    for x in itertools.count(1):
        cube = pow(x, 3)
        cube_digits = ''.join(sorted(str(cube)))

        mapping[cube_digits] += 1
        mapping_sequence[cube_digits].append(cube)

        if mapping[cube_digits] == N:
            result = min(mapping_sequence[cube_digits])
            return result

```
```text
  №      Время  Замедление      Аргумент          Результат
---  ---------  ------------  ----------  -----------------
  1  0.0137154  1.372%                 5       127035954683 (Ответ)
  2  0.13445    12.073%               10    126120833457949
  3  0.990706   85.626%               30  11237467249565803
```
