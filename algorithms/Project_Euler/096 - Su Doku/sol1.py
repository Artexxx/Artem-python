"""
Решите все пятьдесят головоломок, найдите сумму трехзначных чисел, находящихся в верхнем левом углу каждого решения.
Например, 483 является трехзначным числом, находящимся в верхнем левом углу приведенного выше решения.

  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1   0.327112  32.711%             5         1850
  2   3.90085   357.37%            10         4231
  3  18.5256    1462.47%           50        24702
"""
import numpy as np
import sys;sys.path.append('../..')
import importlib

sudoku = importlib.import_module('sudokuSolve[backtracking]')

with open('p096_sudoku.txt') as f:
    lines = f.read().split()

grids = np.empty(shape=(50, 9, 9), dtype='uint8')
for i in range(50):
    for row in range(9):
        for col in range(9):
            grids[i, row, col] = lines[i * 11 + row + 2][col]


def solution(n):
    """
    Решает все пятьдесят головоломок, и возращает сумму трехзначных чисел, находящихся в верхнем левом углу каждого решения.
    """
    result_sum = 0
    for grid in grids[:n]:
        g = grid.tolist()
        if not sudoku.solve(g):
            print("*Error* in solve\n", g)
            break
        first_line = g[0]
        result_sum += first_line[0] * 100 + first_line[1] * 10 + first_line[2]
    return result_sum


if __name__ == '__main__':
    print(solution(50))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [5, 10, 50])
