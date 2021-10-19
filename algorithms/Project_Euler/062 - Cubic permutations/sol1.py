"""
Можно найти перестановки куба 41063625 (345^3), чтобы получить еще два куба: 56623104 (384^3) и 66430125 (405^3).
К слову, 41063625 является наименьшим кубом, для которого ровно три перестановки также являются кубами

Найдите наименьший куб, для которого ровно пять перестановок также являются кубами.

  №      Время  Замедление      Аргумент          Результат
---  ---------  ------------  ----------  -----------------
  1  0.0291759  2.918%                 5       127035954683 (Ответ)
  2  0.149325   12.015%               10    126120833457949
  3  1.07143    92.210%               30  11237467249565803
"""
import itertools


def solution(N):
    """
    Находит наименьший куб, для которого ровно N перестановок также являются кубами.
    """
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


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile;
    TimeProfile(solution, [5, 10, 30])

