"""
Существует 9**81 комбинаций судоки.
Задача:
    Решить судоку.
Идея:
    Ищем пустую клетку и находим для неё число {1-9}|
        - проверяем ошибку по строкам и столбцам    |> <повтор если всё хорошо>
        |> стираем значение и возращаемся на шаг назад
Итог:
    _____________________ Возьмем сложное судоку
    3 * * | * * * | * * *
    * * 5 | * * 9 | * * *
    2 * * | 5 * 4 | * * *
    - - - + - - - + - - -
    * 2 * | * * * | 7 * *
    1 6 * | * * * | * 5 8
    7 * 4 | 3 1 * | 6 * *
    - - - + - - - + - - -
    * * * | 8 9 * | 1 * *
    * * * | * 6 7 | * 8 *
    * * * | * * 5 | 4 3 7

    _____________________ Решённая судоку
    3 9 7 | 6 8 1 | 5 2 4
    6 4 5 | 2 7 9 | 8 1 3
    2 1 8 | 5 3 4 | 9 7 6
    - - - + - - - + - - -
    8 2 3 | 9 5 6 | 7 4 1
    1 6 9 | 7 4 2 | 3 5 8
    7 5 4 | 3 1 8 | 6 9 2
    - - - + - - - + - - -
    4 7 2 | 8 9 3 | 1 6 5
    5 3 1 | 4 6 7 | 2 8 9
    9 8 6 | 1 2 5 | 4 3 7
    Решено за 243098 подстановок
    34950136 function calls (34707038 primitive calls) in 10.576 seconds
"""
from collections import Counter


class Sudoku(object):
    def __init__(self, board):
        self._board = board
        self.count_tries = 0
        self._check_sudoku_validity()

    def solve(self):
        empty = self.get_empty_position()
        if not empty:
            return True
        else:
            row, col = empty
        for number in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            if self.valid_cell(number, (row, col)):
                self[row][col] = number
                self.count_tries += 1

                if self.solve():
                    return True
                else:
                    self[row][col] = 0
        return False

    def valid_cell(self, value, position):
        """
        Проверяет пригодность числа для пустой ячейки
        :param value {1-9} число для проверки
        :param position (строка, столбец) позиция числа
        :return bool
        """
        # Проверка строки
        for i in range(9):
            if self[position[0]][i] == value and position[1] != i:
                return False

        # Проверка столбца
        for i in range(9):
            if self[i][position[1]] == value and position[0] != i:
                return False

        # Проверка квадрата
        for box_item in self.box(*position):
            if box_item == value:
                return False
        return True

    def get_empty_position(self):
        """
        :return координаты пустой ячейки (строка, столбец)
        пустая ячейка - это ячейка заполненая 0
        """
        for i in range(9):
            for j in range(9):
                if self[i][j] == 0:
                    return i, j

    def row_iter(self):
        for i in range(9):
            yield self[i]

    def col_iter(self):
        for i in range(9):
            yield [row[i] for row in self.row_iter()]

    def box(self, row, col):
        box_i = (row // 3) * 3
        box_j = (col // 3) * 3
        for i in range(box_i, box_i + 3):
            for j in range(box_j, box_j + 3):
                yield self[i][j]

    def box_iter(self):
        for i in range(3):
            for j in range(3):
                yield list(self.box(i * 3, j * 3))

    def _check_sudoku_validity(self):
        def check_item(item):
            c = Counter(item)
            if 0 in c: c.pop(0)
            assert all([x == 1 for x in c.values()])

        try:
            for row in self.row_iter():
                check_item(row)
            for col in self.col_iter():
                check_item(col)
            for box in self.box_iter():
                check_item(box)

        except AssertionError:
            raise AssertionError("Судоку решено\введено неправильно")

    def __str__(self):
        str_sudoku = ''
        for i, row in enumerate(self.row_iter()):
            if i % 3 == 0 and i != 0:
                str_sudoku += '- - - + - - - + - - -' + '\n'

            str_row = " "
            for idx, item in enumerate(row):
                if idx % 3 == 0 and idx != 0:
                    str_row += '|' + ' '
                str_row += str(item) + ' '

            str_sudoku += str_row.strip() + '\n'
        return str_sudoku.replace('0', '*')

    def __repr__(self):
        return str(self)

    def __getitem__(self, item):
        return self._board[item]


if __name__ == '__main__':
    def stress_test():
        board = [[3, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 5, 0, 0, 9, 0, 0, 0],
                 [2, 0, 0, 5, 0, 4, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 7, 0, 0],
                 [1, 6, 0, 0, 0, 0, 0, 5, 8],
                 [7, 0, 4, 3, 1, 0, 6, 0, 0],
                 [0, 0, 0, 8, 9, 0, 1, 0, 0],
                 [0, 0, 0, 0, 6, 7, 0, 8, 0],
                 [0, 0, 0, 0, 0, 5, 4, 3, 7]]
        sudoku = Sudoku(board)
        print(sudoku)
        sudoku.solve()
        print('\n________________ Решённая судоку:')
        print(sudoku)
        print(f'Решено за {sudoku.count_tries} подстановок')

    from cProfile import Profile
    with Profile() as pr:
        stress_test()
        pr.print_stats()