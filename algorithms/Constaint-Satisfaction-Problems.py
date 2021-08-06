from typing import Generic, TypeVar, Dict, List, NamedTuple
from abc import ABC, abstractmethod
from string import ascii_uppercase
from random import choice

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Constraint Satisfaction Problem |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
V = TypeVar('Variable (значения переменных)')
D = TypeVar('Domain (области определения)')


class Constraint(Generic[V, D], ABC):
    """
    Базовый класс для всех ограничений
    """

    def __init__(self, variables: List[V]):
        self.variables = variables

    # Метод satisfied переопределяется в подклассах
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]):
        ...


class ConstraintSatisfactionProblem(Generic[V, D]):
    """
    Задача с ограничениями состоит из переменных типа V,
      которые имеют диапазон значений, известные как области определения,
      выбор области определяется для каждой переменоой
    """

    def __init__(self, variables: List[V], domains: [Dict[V, List[D]]]):
        self.variables = variables
        self.domains = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")
        self.assignment_history = []

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        """ Добавляет ограничения D на переменную V"""
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP.")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        """
        Проверяет соответствует ли присваеваемое значение всем ограничениям для данной переменной

        Пример: у нас стоит в методе PositiveConstraint.satisfied (value > 0)
            >>> consistent('b', dict(b = -10))
                 False
        Вывод: мы не можем добавить этой переменной указанную область определения
        """
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Dict[V, D]:
        """
        Задача: нужно найти правильное присваивание для каждой переменной
        Алгоритм:
        1. Находим все переменные, что ещё не назначены
            Выбираем первую и пытаемся присвоить все возможные области определения по очереди
            - если область найдена, сохраняем её в словарь (local_assignment)
        """
        # [Base case] Присваивание завершено, если все переменные назначены
        if len(assignment) == len(self.variables):
            return assignment

        # Все переменные, что еще не назначены
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first: V = unassigned[0]

        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value

            if self.consistent(first, local_assignment):
                self.assignment_history.append(dict(assignment=local_assignment, consistent=True))
                result = self.backtracking_search(local_assignment)
                # [Backtrack] ни с одной областью определения результата небыло найдено
                if result is not None:
                    return result
            else:
                self.assignment_history.append(dict(assignment=local_assignment, consistent=False))
        return None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Pythagorean Triples Constraint Satisfaction Problem |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
Задача: 
  Найти все тройки (x, y, z) такие, что x^2 + y^2 = z^2 и x < y < z и max{x, y, z} < 21.
Переменные:  x, y, z ∈ {1, 2, 3,..., 20}
Домены: домен каждой переменной равен (1, 2, 3, ..., 20)
Ограничения:
    x^2 + y^2 == z^2
    x < y < z
"""


class PythagoreanTriplesConstraint(Constraint):
    """
    Ограничения:
        x^2 + y^2 == z^2
        x < y < z

    >>>pt_con = PythagoreanTriplesConstraint(['x', 'y', 'z'])
    >>>pt_con.satisfied(dict(x=3, y=4, z=5))
    True
    """

    def satisfied(self, assignment: dict):
        values = list(assignment.values())
        pythagorean_triple_constraint = values[0] ** 2 + values[1] ** 2 == values[2] ** 2 if len(values) == 3 else True
        total_order_constraint = values[0] < values[1] < values[2] if len(values) == 3 else True
        return pythagorean_triple_constraint and total_order_constraint


if __name__ == '__main__':
    pt_con = PythagoreanTriplesConstraint(['x', 'y', 'z'])
    pt_con.satisfied(dict(x=3, y=4, z=5))  # => True

    testPTripletCSP = ConstraintSatisfactionProblem(
        variables=['x', 'y', 'z'],
        domains=dict(x=list(range(1, 21)),
                     y=list(range(1, 21)),
                     z=list(range(1, 21)))
    )
    testPTripletCSP.add_constraint(PythagoreanTriplesConstraint(['x', 'y', 'z']))
    solutionMS = testPTripletCSP.backtracking_search(assignment={'x': 5})
    if solutionMS is None:
        print("No solution found!")
    else:
        print(solutionMS)  # RESULTS: (x: 3 y: 4 z: 5) (x: 5 y: 12 z: 13)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Magic Square Constraint Satisfaction Problem |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
Задача: 
  Заполните квадрат n x n различными целыми положительными числами в диапазоне (1, ..., n x n) так чтобы
  каждая ячейка содержала уникальное целое число, и сумма целых чисел в каждой строке, столбце и диагонали была одинаковой.

Подсказка:
  Магическую сумма, определяется по формуле n * ((n * n + 1) / 2).


Variables: квадраты на доске.
Domain: область определения каждой переменной равена (1,..., n x n).
Constraints:
    Каждая переменная должна иметь уникальное значение.
    Значения всех строк суммируются до магической суммы.
    Значения всех столбцов суммируются до магической суммы.
    Значения обеих диагоналей суммируются до магической суммы.
"""


class ExactLengthExactSum:
    """
    Возвращает True если N переменных суммируются до sum_value
    [*] Возвращает True если количество переменных меньше N
    """

    def __init__(self, number_of_values: int, sum_value) -> None:
        self.__number_of_values = number_of_values
        self.__sum_value = sum_value

    def __call__(self, values: tuple) -> bool:
        if len(values) < self.__number_of_values:
            return True
        if len(values) == self.__number_of_values:
            return sum(values) == self.__sum_value
        if len(values) > self.__number_of_values:
            return False


class MSTableConstraints:
    """
    Делает проверку table, размером NxN, в соответствии с правилами магических квадратов
    [*] таблица задаётся словарём Пример: {1: 2, 2: 7, 3: 6 ... 8: 3, 9: 8}
    [*] Строка, столбец или диагональ не проверяются если в них находится хотя-бы один пустой символ (-1)

    >>> t = {1: 2, 2: 7, 3: 6, 4: 9, 5: 5, 6: 1, 7: 4, 8: 3, 9: 8}
    ... MSTableConstraints(t, 3).check_table()
    True
    """

    def __init__(self, table: dict, n: int) -> None:
        self.__table = table
        self.__n = n
        self.__order = n * n
        self.__null_number = -1

    def _check_raws(self):
        for row in range(1, self.__order + 1, self.__n):
            row_data = [(self.__table[i]) for i in range(row, row + self.__n)]
            if self.__null_number not in row_data:
                if not ExactLengthExactSum(row_data):
                    return False
        return True

    def _check_columns(self):
        for column in range(1, self.__n + 1):
            column_data = [(self.__table[i]) for i in range(column, order + 1, n)]
            if self.__null_number not in column_data:
                if not ExactLengthExactSum(column_data):
                    return False
        else:
            return True

    def _check_right_diagonal(self):
        right_diag = [self.__table[diag] for diag in range(1, self.__order + 1, self.__n + 1)]
        if self.__null_number in right_diag:
            return True
        else:
            return ExactLengthExactSum(right_diag)

    def _check_left_diagonal(self):
        left_diag = [self.__table[diag] for diag in range(self.__n, self.__order, self.__n - 1)]
        if self.__null_number in left_diag:
            return True
        else:
            return ExactLengthExactSum(left_diag)

    def check_table(self):
        return all((self._check_raws(),
                    self._check_columns(),
                    self._check_columns(),
                    self._check_left_diagonal(),
                    self._check_right_diagonal()
                    ))


def all_diff_constraint_evaluator(values: tuple) -> bool:
    seen_values = set()
    for val in values:
        if val in seen_values:
            return False
        seen_values.add(val)
    return True


class MagicSquareConstraint(Constraint):
    """
    Каждая переменная должна иметь уникальное значение.
    Значения всех строк суммируются до магической суммы.
    Значения всех столбцов суммируются до магической суммы.
    Значения обеих диагоналей суммируются до магической суммы.
    """
    n = 3
    count = 1

    def satisfied(self, assignment: dict):
        if not all_diff_constraint_evaluator(list(assignment.values())):
            return False
        MagicSquareConstraint.count += 1
        if len(assignment) < 9:
            # пустуе клетки заполняются -1 и комюинации с ними не будут проверяться
            raw_assignment = {i: assignment.get(i, -1) for i in range(1, MagicSquareConstraint.n ** 2 + 1)}
            raw_table_MS = MSTableConstraints(raw_assignment, n=MagicSquareConstraint.n)
            return raw_table_MS.check_table()
        elif len(assignment) == 9:
            # пустых  клеток нет - можно смело проверять весь квадрат
            table_MS = MSTableConstraints(assignment, n=MagicSquareConstraint.n)
            return table_MS.check_table()


if __name__ == '__main__':
    n = 3
    order = n ** 2
    magic_sum = n * int((order + 1) / 2)
    name_to_variable_map = {square: list(range(1, order + 1)) for square in range(1, order + 1)}

    # Так специально сделано, чтобы не передавть n и magic_sum каждый раз
    ExactLengthExactSum = ExactLengthExactSum(n, magic_sum)

    ms_con = MagicSquareConstraint(list(range(1, order + 1)))
    ms_con.n = n
    print(ms_con.satisfied({1: 2, 2: 7, 3: 6, 4: 9, 5: 5, 6: 1, 7: 4, 8: 3, 9: 8}))  # => True

    testMSCSP = ConstraintSatisfactionProblem(
        variables=list(range(1, order + 1)),
        domains=name_to_variable_map
    )
    testMSCSP.add_constraint(MagicSquareConstraint(list(range(1, order + 1))))
    solutionMS = testMSCSP.backtracking_search(assignment={1: 8})
    if solutionMS is None:
        print("No solution found!")
    else:
        print(solutionMS)  # RESULTS: {1: 8, 2: 1, 3: 6, 4: 3, 5: 5, 6: 7, 7: 4, 8: 9, 9: 2}
        print("Число ходов:", MagicSquareConstraint.count)  # Число ходов: 62



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Map Coloring Problem |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
Задача:
    Раскрасить карту в 3 цвета таким образом, чтобы каждая из 7 территорий не соседствовала с территорией того же цвета.
 
Variables: 7 территорий.
Domains: область определения каждой переменной равен 3 цветам.
Constraints:
     Две соседних территории не должны иметь один и тот же цвет.
"""


class MapColoringConstraint(Constraint[str, str]):
    """
    Проверяет, имеют ли две территории один и тот же цвет.

    >>> mcc = MapColoringConstraint('a', 'b')
    mcc.satisfied(dict(a='blue', b='red'))  # => True
    >>> mcc.satisfied(dict(a='orange', b='orange'))  # => False
    """

    def __init__(self, place1: str, place2: str):
        super().__init__([place1, place2])
        self.place1 = place1
        self.place2 = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        if assignment[self.place1] == assignment[self.place2]:
            return False
        return True


if __name__ == '__main__':
    testMCC = MapColoringConstraint('a', 'b')
    testMCC.satisfied(dict(a='blue', b='red'))  # => True
    testMCC.satisfied(dict(a='orange', b='orange'))  # => False

    variables: List[str] = ["Western Australia", "Northern Territory", "South Australia", "Queensland",
                            "New South Wales", "Victoria", "Tasmania"]
    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = ["red", "green", "blue"]
    map_coloring_csp = ConstraintSatisfactionProblem(variables, domains)

    map_coloring_csp.add_constraint(MapColoringConstraint("Western Australia", "Northern Territory"))
    map_coloring_csp.add_constraint(MapColoringConstraint("Western Australia", "South Australia"))
    map_coloring_csp.add_constraint(MapColoringConstraint("South Australia", "Northern Territory"))
    map_coloring_csp.add_constraint(MapColoringConstraint("Queensland", "Northern Territory"))
    map_coloring_csp.add_constraint(MapColoringConstraint("Queensland", "South Australia"))
    map_coloring_csp.add_constraint(MapColoringConstraint("Queensland", "New South Wales"))
    map_coloring_csp.add_constraint(MapColoringConstraint("New South Wales", "South Australia"))
    map_coloring_csp.add_constraint(MapColoringConstraint("Victoria", "South Australia"))
    map_coloring_csp.add_constraint(MapColoringConstraint("Victoria", "New South Wales"))
    map_coloring_csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))

    map_coloring_csp.consistent('Western Australia', {'Western Australia': 'red',
                                                      'Northern Territory': 'red'})  # => False
    map_coloring_csp.consistent('Western Australia', {'Western Australia': 'red',
                                                      'Northern Territory': 'blue'})  # => True

    solution = map_coloring_csp.backtracking_search(assignment={'Victoria': 'green'})



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Eight Queens Problem |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
Задача:
    Каждая королева должна быть помещена на шахматную доску, не атакуя других.
    Королевы могут двигаться вдоль любой строки, столбца, диагонали и не должны иметь возможности атаковать друг друга.

Variables: столбцы доски.
Domains: 
    равен строке, в которой каждая королева может быть помещена в столбец, 
    т. е. область определения каждой переменной равена (1, ..., n).
"""


class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        # q1c = queen 1 column, q1r = queen 1 row
        for q1c, q1r in assignment.items():
            # q2c = queen 2 column
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]  # q2r = queen 2 row
                    if q1r == q2r:  # same row?
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):  # same diagonal?
                        return False
        return True  # no conflict


if __name__ == "__main__":
    columns = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    testQuinsCSP = ConstraintSatisfactionProblem(columns, rows)
    testQuinsCSP.add_constraint(QueensConstraint(columns))
    q_solution = testQuinsCSP.backtracking_search(assignment={1: 4})  # {1: 1, 2: 5, 3: 8, 4: 6, 5: 3, 6: 7, 7: 2, 8: 4}



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Word Search Constraint Satisfaction Problem |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
Дана сетка букв со скрытыми словами, расположенных по строкам, столбцам и диагоналям.
Задача:
    Даны слова, надо их все разместить в сетке
Variables: это слова
Domains: оласть определени слова состоит из списока списков возможных положений всех его букв   
Constraints:
    Слова должны распологаться в пределах строки, столбца или диагонали в пределах сетки
     и не должны перекрывать друг друга
"""


class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(rows: int, columns: int):
    """
    Заполняет сетку случайными буквами

    >>> generate_grid(11, 11)
    """
    return [[choice(ascii_uppercase)
             for _ in range(columns)]
            for _ in range(rows)]


def display_grid(grid) -> None:
    for row in grid: print("".join(row))


def generate_domain(word, grid):
    """
    Каждое слово имеет домен (область определения), который представляет собой
    список списков допустимых местоположений для каждой буквы в слове.

    Пример:      |x x x x x|
        grid  =  |x x x x x|
        word = "WORD"
        Существует всего 4 варианта расположения этого слова в таблице 2x4
        |W O R D x| or |x W O R D|
        |W O R D x|    |x W O R D|

    >>> grid =  [["x", "x", "x", "x", 'x']]*2
    >>>generate_domain("WORD", grid])
    [
    (row=0, column=0) to (row=0, column=4)
    (row=0, column=1) to (row=0, column=5)
    (row=1, column=0) to (row=1, column=4)
    (row=1, column=1) to (row=1, column=5)
    ]
    """
    domain = []
    height = len(grid)
    width = len(grid[0])
    length = len(word)

    for row in range(height):
        for col in range(width):
            columns = range(col, col + length + 1)
            rows = range(row, row + length + 1)
            if col + length <= width:
                # Left to right
                domain.append([GridLocation(row, c) for c in columns])
                # Diagonal towards bottom right
                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])

            if row + length <= height:
                # Top to bottom
                domain.append([GridLocation(r, col) for r in rows])
                # Diagonal towards bottom left
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])

    return domain


class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words: List[str]) -> None:
        super().__init__(words)
        self.words: List[str] = words

    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        # если есть какие-либо дубликаты расположения сетки, то есть перекрытие
        all_locations = [locs for values in assignment.values()
                         for locs in values]
        return len(set(all_locations)) == len(all_locations)


if __name__ == "__main__":
    grid = generate_grid(9, 9)
    words = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations: Dict[str, List[List[GridLocation]]] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    csp = ConstraintSatisfactionProblem(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Verbal Arithmetic |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
Дана криптографическая головоломка, где нужно найти такие цифры, которые, 
будучи подставленными вместо букв, сделают математическое утверждение верным 
Задача:
    Дано матиматическое выражение, состоящее из слов. Каждая буква в задаче - одна цифра от 0 до 9.
    Никакие две разные буквы не могут представлять одну и туже цифру. 
    Если буква повторяется, это означает, что цифра в решении также повторяется.
Пример:
    Дано:  SEND + MORE = MONEY
    Ответ: 9567 + 1085 = 10652
    
Variables: это буквы слова
Domains: область определения каждой буквы состоит из цифр от 0 до 9   
Constraints:
    Никакие две разные буквы не могут представлять одну и туже цифру. 
    При подстановки цифр вместо букв, математичское выражение должно быть истино
"""

class SendMoreMoneyConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters = letters

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # Никакие две разные буквы не могут представлять одну и туже цифру.
        if len(set(assignment.values())) < len(assignment):
            return False

        if len(assignment) == len(self.letters):
            s = assignment["S"]
            e = assignment["E"]
            n = assignment["N"]
            d = assignment["D"]
            m = assignment["M"]
            o = assignment["O"]
            r = assignment["R"]
            y = assignment["Y"]
            send = s * 1000 + e * 100 + n * 10 + d
            more = m * 1000 + o * 100 + r * 10 + e
            money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
            return send + more == money
        return True


if __name__ == "__main__":
    letters = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    possible_digits: Dict[str, List[int]] = {}
    for letter in letters:
        possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_digits["M"] = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # таким образом, мы не получаем ответов, начинающихся с 0
    csp = ConstraintSatisfactionProblem(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)  # {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}