"""
Можно найти перестановки куба 41063625 (345^3), чтобы получить еще два куба: 56623104 (384^3) и 66430125 (405^3).
К слову, 41063625 является наименьшим кубом, для которого ровно три перестановки также являются кубами

Найдите наименьший куб, для которого ровно пять перестановок также являются кубами.

  №      Время  Замедление      Аргумент          Результат
---  ---------  ------------  ----------  -----------------
  1  0.0137154  1.372%                 5       127035954683 (Ответ)
  2  0.13445    12.073%               10    126120833457949
  3  0.990706   85.626%               30  11237467249565803
"""
import itertools
from collections import defaultdict


def solution(N):
    """
    Находит наименьший куб, для которого ровно N перестановок также являются кубами.
    """
    mapping = defaultdict(int)
    cubes = defaultdict(list)

    for x in itertools.count(1):
        cube = pow(x, 3)
        cube_digits = ''.join(sorted(str(cube)))

        mapping[cube_digits] += 1
        cubes[cube_digits].append(cube)

        if mapping[cube_digits] == N:
            result = min(cubes[cube_digits])
            return result


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile;
    TimeProfile(solution, [5, 10, 30])

