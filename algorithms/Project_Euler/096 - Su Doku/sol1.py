"""
Решите все пятьдесят головоломок, найдите сумму трехзначных чисел, находящихся в верхнем левом углу каждого решения.
Например, 483 является трехзначным числом, находящимся в верхнем левом углу приведенного выше решения.

  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1   0.327112  32.711%             5         1850
  2   3.90085   357.37%            10         4231
  3  18.5256    1462.47%           50        24702
"""


class Sudoku(object):
    def __init__(self, board):
        self._board = board
        self.count_tries = 0

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
        :param number {1-9} — число для проверки
        :param position (строка, столбец) — позиция числа
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
        пустая ячейка - это ячейка заполненная 0
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

    def __str__(self):
        str_sudoku = str()

        for i, row in enumerate(self.row_iter()):
            if i % 3 == 0 and i != 0:
                str_sudoku += '- - - + - - - + - - -' + '\n'
            str_row = " "

            for idx, item in enumerate(row):
                if idx % 3 == 0 and idx != 0:
                    str_row += '|' + ' '
                str_row += str(item) + ' '

            str_sudoku += str_row.strip() + '\n'
        return str_sudoku.replace('0', '.')

    def __repr__(self):
        return f'Sudoku({self._board})'

    def __getitem__(self, item):
        return self._board[item]


def get_first_n_boards_from_file(n, file_name="p096_sudoku.txt"):
    with open(file_name) as f:
        lines = f.read().split()

    for i in range(n):
        board = []
        for row in range(9):
            board.append(
                list(map(int, lines[i * 11 + row + 2]))
            )
        yield board
    return n


def solution(N):
    """
    Решает первые N головоломок и возвращает сумму трехзначных чисел, находящихся в верхнем левом углу каждого решения.
    """
    result_sum = 0
    for board in get_first_n_boards_from_file(N):
        sudoku = Sudoku(board)
        sudoku.solve()
        first_line = sudoku[0]
        result_sum += first_line[0] * 100 + first_line[1] * 10 + first_line[2]
    return result_sum


if __name__ == '__main__':
    # print(solution(50))
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [5, 10, 50])
