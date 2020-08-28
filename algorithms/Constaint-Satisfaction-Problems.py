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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Simple Example |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class PositiveConstraint(Constraint):
    """
    Простое ограничение, которое проверяет, является ли значение положительным.
    """

    def satisfied(self, assignment: dict):
        for value in assignment.values():
            if value < 0:
                return False
        return True


if __name__ == '__main__':
    pos_con = PositiveConstraint(['a', 'b', 'c', 'd'])
    pos_con.satisfied(dict(a=-1))  # => False
    pos_con.satisfied(dict(a=2))  # => True

    testCSP = ConstraintSatisfactionProblem(
        variables=['a', 'b', 'c', 'd'],
        domains=dict(a=[1, 2, 3],
                     b=[4, 5, 6],
                     c=[7, 8, 9],
                     d=[10, 11, 12])
    )
    testCSP.consistent('a', dict(a=1))  # => True
    testCSP.consistent('b', dict(b=-1))  # => False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Map Coloring Problem |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""Задача:
 Раскрасить карту в 3 цвета таким образом, чтобы каждая из 7 территорий не соседствовала с территорией того же цвета.
"""


class MapColoringConstraint(Constraint[str, str]):
    """
    Проверяет, имеют ли две территории один и тот же цвет.

    >>> mcc = MapColoringConstraint('a', 'b')
    ... mcc.satisfied(dict(a='blue', b='red'))  # => True
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
                                                      'Northern Territory': 'red'})  # => False                                                   'Northern Territory': 'red'})
    map_coloring_csp.consistent('Western Australia', {'Western Australia': 'red',
                                                      'Northern Territory': 'blue'})  # => True

    solution = map_coloring_csp.backtracking_search(assignment={'Victoria': 'green'})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Eight Queens Problem |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""Задача:
 Каждая королева должна быть помещена на шахматную доску, не атакуя других.
 Королевы могут двигаться вдоль любой строки, столбца, диагонали и не должны иметь возможности атаковать друг друга.
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
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    testQuinsCSP = ConstraintSatisfactionProblem(columns, rows)
    testQuinsCSP.add_constraint(QueensConstraint(columns))
    solution = testQuinsCSP.backtracking_search()  # {1: 1, 2: 5, 3: 8, 4: 6, 5: 3, 6: 7, 7: 2, 8: 4}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Word Search Constraint Satisfaction Problem |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
Дана сетка букв со скрытыми словами, расположенных по строкам, столбцам и дифгоналям.
Задача:
    Даны слова, надо их все разместить в сетке
Примечания:
    V (переменные) - это слова
    D (области определения) - возможные их положения
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
