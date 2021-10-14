"""
К фигурным (многоугольным) числам относятся треугольные, квадратные, пятиугольные, шестиугольные, семиугольные и восьмиугольные числа, которые расчитываются по следующим формулам:

     | Название         | Формула         | Пример               |
     | ----             | ----            | :-----               |
     | Треугольные	 	|P3,n=n(n+1)/2	  |	1, 3, 6, 10, 15, ... |
     | Квадратные	 	|P4,n=n2	 	  |1, 4, 9, 16, 25, ...  |
     |Пятиугольные	 	|P5,n=n(3n−1)/2	  |	1, 5, 12, 22, 35, ...|
     | Шестиугольные	|P6,n=n(2n−1)     |	1, 6, 15, 28, 45, ...|
     | Семиугольные	    |P7,n=n(5n−3)/2	  |	1, 7, 18, 34, 55, ...|
     |Восьмиугольные	|P8,n=n(3n−2)     |	1, 8, 21, 40, 65, ...|

 Упорядоченное множество из трех четырехзначных чисел: 8128, 2882, 8281, обладает тремя интересными свойствами
Множество является цикличным: последние две цифры каждого числа являются первыми двумя цифрами следующего (включая последнее и первое числа).
Каждый тип многоугольника — треугольник (P3,127=8128), квадрат (P4,91=8281) и пятиугольник (P5,44=2882) — представлены различными числами данного множества.
Это — единственное множество четырехзначных чисел, обладающее указанными свойствами.
Найдите сумму элементов единственного упорядоченного множества из шести цикличных четырехзначных чисел, в котором каждый тип многоугольников — треугольник, квадрат, пятиугольник, шестиугольник, семиугольник и восьмиугольник — представлены различными числами этого множества.
 
 Упорядоченное множество из трех четырехзначных чисел: 8128, 2882, 8281, обладает тремя интересными свойствами
 
 Множество является цикличным: последние две цифры каждого числа являются первыми двумя цифрами следующего (включая последнее и первое числа).
Каждый тип многоугольника — треугольник (P3,127=8128), квадрат (P4,91=8281) и пятиугольник (P5,44=2882) — представлены различными числами данного множества.
Это — единственное множество четырехзначных чисел, обладающее указанными свойствами.
Найдите сумму элементов единственного упорядоченного множества из шести цикличных четырехзначных чисел, в котором каждый тип многоугольников — треугольник, квадрат, пятиугольник, шестиугольник, семиугольник и восьмиугольник — представлены различными числами этого множества.
"""
from itertools import islice
from operator import itemgetter
from typing import List, Tuple, Set, NewType, Iterator

Polygonal = NewType('Polygonal', int)
TypePolygonal = NewType('TypePolygonal', int)
IndexPolygonal = NewType('IndexPolygonal', int)


def generate_polygonal(type_number: TypePolygonal) -> Iterator[Polygonal]:
    """Генерирует фиругные числа, тип числа задается через type_number.

    >>> generate_polygonal(type_number=3)
    1 3 6 10 15 21 28 36 [...]
    >>> generate_polygonal(type_number=4)
    1 4 9 16 25 36 49 64 [...]
    """
    c = type_number - 2
    a = b = 1

    while True:
        yield a
        b += c
        a += b


def is_cyclic(x: Polygonal, y: Polygonal):
    """Возвращает True, если последние две цифры первого числа являются первыми двумя цифрами второго числа"""
    return x % 100 == y // 100


def solution():
    """
    Находит сумму элементов единственного упорядоченного множества из шести цикличных четырехзначных чисел.
    """
    numbers = (
        tuple(islice(generate_polygonal(3), 45, 141)),  # Triangle	  1, 3, 6, 10, 15,  ...
        tuple(islice(generate_polygonal(4), 31, 100)),  # Square	  1, 4, 9, 16, 25,  ...
        tuple(islice(generate_polygonal(5), 25, 82)),   # Pentagonal  1, 5, 12, 22, 35, ...
        tuple(islice(generate_polygonal(6), 22, 71)),   # Hexagonal   1, 6, 15, 28, 45, ...
        tuple(islice(generate_polygonal(7), 20, 64)),   # Heptagonal  1, 7, 18, 34, 55, ...
        tuple(islice(generate_polygonal(8), 18, 59))    # Octagonal   1, 8, 21, 40, 65, ...
    )

    def get_number(path: Tuple[TypePolygonal, IndexPolygonal]) -> Polygonal:
        return numbers[path[0]][path[1]]

    typegetter = itemgetter(0)
    types: Set[TypePolygonal] = set(range(6))

    def search(path: List[Tuple[TypePolygonal, IndexPolygonal]]):
        if len(path) == 6:
            if is_cyclic(get_number(path[-1]),
                         get_number(path[0])):
                return path
            else:
                return 0

        unused_types = types - set(map(typegetter, path))
        this_number = get_number(path[-1])

        for u in unused_types:
            for k in range(len(numbers[u])):
                if is_cyclic(this_number, numbers[u][k]):
                    s = search(path + [(u, k)])
                    if s: return s

    # Start from the octagonal numbers
    for index in range(len(numbers[5])):
        path = search([(5, index)])
        if path:
            return sum(map(get_number, path))


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import cProfile

    with cProfile.Profile() as pr:
        print(solution())
        print('\n\n');
        pr.print_stats()
