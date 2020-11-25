from enum import Enum
from typing import List, NamedTuple, Deque
import random
from heapq import heappush, heappop


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Создание лабиринта|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    END = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows=10, columns=10, sparseness=0.2,
                 start=MazeLocation(0, 0), end=MazeLocation(9, 9)):
        self._rows = rows
        self._columns = columns
        self.start = start
        self.end = end
        # заполнение сетки пустыми ячейками
        self._grid = [[Cell.EMPTY
                       for _ in range(columns)]
                      for _ in range(rows)]
        # заполнение сетки заблокированными ячейками (препядствиями)
        self._randomly_fill(rows, columns, sparseness)
        # заполнение начальной и конечной позиции в лабиринте
        self._grid[start.row][start.column] = Cell.START
        self._grid[end.row][end.column] = Cell.END

    def _randomly_fill(self, rows, columns, sparseness: float):
        """
        Заполнеи сетку заблокированными ячейками (препядствиями)
        """
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        """
        Выводит красиво отформатированную версию лабиринта для печати
        >>> new_maze = Maze()
        ... print(new_maze)
        """
        output = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output

    def end_test(self, ml: MazeLocation) -> bool:
        """
        Сравнивает координаты ml c финишными координатами self.end
        """
        return ml == self.end

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        """
        Проверяет верхнюю, нижнюю, правую и левую смежные ячейки по отношению к MazeLocation в Maze,
        чтобы увидеть есть ли там пустые места в которые можно попасть из ячейки ml
        """
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        return locations

    def mark(self, path: List[MazeLocation]):
        """
        Помечает клетки с координатами из масива path как пройденные (Cell.PATH)
        """
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.end.row][self.end.column] = Cell.END

    def clear(self, path: List[MazeLocation]):
        """
        Чистит клетки с координатами из масива path (Cell.EMPTY)
        """
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.end.row][self.end.column] = Cell.END


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Функции для создания пути |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class Node():
    """
    Помогает при переходе из одного состояния (клетки) в другое:

    >>> current_node.state() #=> MazeLocation(row=9, column=9)
    ... current_node.parent.state() #=> MazeLocation(row=9, column=8)
    """

    def __init__(self, state, parent, cost: float = 0.0, heuristic: float = 0.0):
        """
        [*] cost и heuristic необходимы для очереди с приоритетом

        cost (float) - функция затрат `g(n)` - количество сделанных шагов от начальной клетки до заданной (активной)
        heuristic (float) - эвристическая функция `h(n)` - затраты для того чтобы добраться из заданной (активной) клетки до конечной
        """
        self.state = state
        self.parent: Node = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def node_to_path(node: Node) -> List[MazeLocation]:
    """
    Возращает координаты пути от начальной до конечной ячейки.
    """
    path = [node.state]
    # Двигается назад (от конца к началу)
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Поиск в глубину|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class Stack():
    def __init__(self) -> None:
        self._container = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


def depth_first_search(initial, end_test, successors) -> Node:
    """
    Во время поиска в глубину будут отслеживаться две структуры данных:
    1. frontier - стэк рассматриваемых состояний (клетки куда надо сходить)
    2. explored - набор рассматренных состояний (клетки куда уже сходили)
    Алгоритм:
        Пока в frontier есть состояния - искать цель поиска
        Помечать все просмотренные состояния как explored
        - Если frontier станет пустым -> объектов для поиска не осталось

    [-] не старается найти кратчайшмй путь
    """
    frontier = Stack()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if end_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None  # путей не найдено


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Поиск в ширину|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class Queue():
    def __init__(self) -> None:
        self._container = Deque()

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

    def __repr__(self) -> str:
        return repr(self._container)


def breadth_first_search(initial, end_test, successors) -> Node:
    """
    Во время поиска в ширину будут отслеживаться две структуры данных:
    1. frontier - очередь рассматриваемых состояний (клетки куда надо сходить)
    2. explored - набор рассматренных состояний (клетки куда уже сходили)
    Алгоритм:
        Пока в frontier есть состояния - искать цель поиска
        Помечать все просмотренные состояния как explored
        - Если frontier станет пустым -> объектов для поиска не осталось

    [+] всегда находит кратчайшмй путь
    """
    frontier = Queue()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if end_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None  # путей не найдено


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Поиск по алгоритму А*|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class PriorityQueue:
    def __init__(self) -> None:
        self._container = []

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        """Поместить в очередь по приоритету"""
        heappush(self._container, item)

    def pop(self):
        """Извлечь по приоритету"""
        return heappop(self._container)

    def __repr__(self):
        return repr(self._container)


def manhattan_distance(end: MazeLocation):
    """Возращает Манхэттенское расстояние между 2 точками

    >>> end, b = MazeLocation(4, 4), MazeLocation(0, 4)
    ... manhattan_distance(end)(b)
    4.0
    """

    def distance(ml: MazeLocation) -> float:
        xdist = abs(ml.column - end.column)
        ydist = abs(ml.row - end.row)
        return (xdist + ydist)

    return distance


def aStar(initial, end_test, successors, heuristic) -> Node:
    """
    Во время поиска по алгоритму A* каждому новому узлу назначаются затраты,
     основанные на формуле расстояния, а также эвристический показатель.

    Отслеживаются две структуры данных:
    1. frontier - очередь c приоритетом рассматриваемых состояний (клетки куда хотим сходить)
    2. explored - словарь рассматренных состояний (клетки куда уже сходили и их веса)
    Алгоритм:
        Пока в frontier есть состояния -
            Выбираем в какую из клеток направиться g(n)+h(n)
        Помечать все просмотренные состояния как explored
        - Если frontier станет пустым -> объектов для поиска не осталось

    [*] Может сходить два раза по одной клетке (если затраты меньше)
    [+] Всегда находит кратчайшмй путь
    """
    frontier = PriorityQueue()
    frontier.push(Node(initial, None))
    explored = {initial: 0.0}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if end_test(current_state):
            return current_node
        for child in successors(current_state):
            new_cost = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None  # путей не найдено


if __name__ == "__main__":
    m: Maze = Maze()
    print(m)

    # Тестирование DFS
    solution = depth_first_search(m.start, m.end_test, m.successors)
    if solution is None:
        print("Используя поиск в глубину решения не было найдено")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        print(f"[DFS] Потребовалось {len(path)} ходов.\n")
        m.clear(path)

    # Тестирование BFS
    solution = breadth_first_search(m.start, m.end_test, m.successors)
    if solution is None:
        print("Используя поиск в ширину решения не было найдено")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        print(f"[BFS] Потребовалось сделать {len(path)} ходов.\n")
        m.clear(path)

    # Тестирование A*
    solution = aStar(m.start, m.end_test, m.successors, heuristic=manhattan_distance(m.end))
    if solution is None:
        print("Используя поиск алгоритмом А* решения не было найдено")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        print(f"[А*] Потребовалось сделать {len(path)} ходов.\n")
        m.clear(path)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Двунаправленный поиск в ширину |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
"""
Учитывая два слова (beginWord и endWord) и список слов, найдите длину кратчайшей последовательности преобразований от beginWord до endWord, такую что:
За один раз можно изменить только одну букву
Каждое промежуточное слово должно существовать в списке слов

Например дано:
    beginWord = "hit"
    endWord = "cog"
    список слов = ["hot","dot","dog","lot","log"]
Поскольку одним из самых коротких преобразований является  "hit" -> "hot" -> "dot" -> "dog" -> "cog", верните его длину 5.

Примечание:
    - Верните 0, если такой последовательности преобразований не существует
    - Все слова имеют одинаковую длину.
    - Все слова содержат только строчные буквы алфавита.
"""

def ladderLength(beginWord, endWord, wordList):
    beginSet = set()
    endSet = set()
    beginSet.add(beginWord)
    endSet.add(endWord)
    result = 2
    while len(beginSet) != 0 and len(endSet) != 0:
        if len(beginSet) > len(endSet):
            beginSet, endSet = endSet, beginSet
        nextBeginSet = set()
        for word in beginSet:
            for ladderWord in wordRange(word):
                if ladderWord in endSet:
                    return result
                if ladderWord in wordList:
                    nextBeginSet.add(ladderWord)
                    wordList.remove(ladderWord)
        beginSet = nextBeginSet
        result += 1
    return 0


def wordRange(word):
    for ind in range(len(word)):
        tempC = word[ind]
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c != tempC:
                yield word[:ind] + c + word[ind + 1:]

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "coc"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(ladderLength(beginWord, endWord, wordList))