from dlxsudoku.sudoku import Sudoku

from timeit import default_timer as timer
s = [l for l in open('p096_sudoku.txt').readlines() if l[0].isdigit()]
sudokus = [Sudoku(''.join(s[i * 9:(i + 1) * 9])) for i in range(50)]
t = timer()
for sudoku in sudokus:
    sudoku.solve()

result = sum(int(sudoku.to_oneliner()[:3]) for sudoku in sudokus)
print(timer()-t)
print(result)