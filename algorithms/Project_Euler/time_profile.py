from tabulate import tabulate
from timeit import default_timer as timer


def my_time_this(function, test_numbers: list):
    """
Оценивает время работы 1 алгоритма

|------------------------------+-------------------|
|          Полином             |  Функции          |
|------------------------------+-------------------|
| 1.00  log2(N)   +  1.25e-015 | N                 |
| 2.00  log2(N)   +  5.31e-018 | N*N               |
| 1.19  log2(N)   +      1.116 | N*log2(N)         |
| 1.37  log2(N)   +      2.232 | N*log2(N)*log2(N) |

>>> my_time_this(solution, [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000])

№      Время  Замедление        Число         Результат
---  ---------  ------------  ---------  ----------------
  1  0.0008448  0.084%            10000          23331668
  2  0.0084711  0.763%           100000        2333316668
  3  0.095528   8.706%          1000000      233333166668
  4  0.9545     85.897%        10000000    23333331666668
  5  9.6361     868.160%      100000000  2333333316666668
"""
    def calc_result(function, number):
        t = timer()
        my_time_this.last_result = function(number)
        my_time_this.last_time = timer() - t

    data = []
    for index, number in enumerate(test_numbers):
        calc_result(function, number)
        if index >= 1:
            slowdown = f"{(my_time_this.last_time - data[-1][1]):.2%}"
        else:
            slowdown = f"{my_time_this.last_time:.3%}"
        data.append([index + 1, my_time_this.last_time, slowdown, number, my_time_this.last_result])
    print(tabulate(data, headers=["№", "Время", "Замедление", "Число", "Результат"]))
