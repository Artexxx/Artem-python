import math
import sys
import time
import threading
import itertools

from tabulate import tabulate
from timeit import default_timer as timer
import os


class ParallelTimer:
    timer_is_running = False
    _timer_has_run_FLAG = False

    timer_time = 0.0

    def start_parallel_timer(self):
        self._timer_has_run_FLAG = True
        self.timer_is_running = True

        self.parallel_timer_task = threading.Thread(target=self._parallel_timer)
        self.parallel_timer_task.start()

    def stop_parallel_timer(self):  # FIXME (How stop parallel task?)
        self._timer_has_run_FLAG = False
        self.parallel_timer_task.join()

        while self.timer_is_running:
            time.sleep(0.05)
        print(f"\rТаймер закончил работу, время = {self.timer_time:.3}s", end='\n\n')

    def _parallel_timer(self):
        t = timer()
        self.timer_time = 0.0
        phases = itertools.cycle(['◑', '◒', '◐', '◓'])

        while self._timer_has_run_FLAG:
            sys.stdout.write(f"\rВремя работы {next(phases)} {self.timer_time:.4}s")
            sys.stdout.flush()
            time.sleep(0.05)
            self.timer_time = timer() - t
        else:
            self.timer_is_running = False

    def __enter__(self):
        self.start_parallel_timer()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_parallel_timer()
        return self


class TimeProfile:
    """
    Оценивает время работы 1 алгоритма

    ┌──────────────────────────────┬───────────────────┐
    │          Полином             │  Функция          │
    │------------------------------│-------------------│
    │ 1.00  log2(N)   +  1.25e-015 │ N                 │
    │ 2.00  log2(N)   +  5.31e-018 │ N*N               │
    │ 1.19  log2(N)   +      1.116 │ N*log2(N)         │
    │ 1.37  log2(N)   +      2.232 │ N*log2(N)*log2(N) │

    ┌────────────┬─────────────────────────────────────────────┐
    │  Notation  │                 Type                        │
    │------------│---------------------------------------------│
    │ O(1)       │ Constant. Does not depend on the input data.│
    │ O(n)       │ Linear. Will grow as "n" grows.             │
    │ O(n log n) │ Quasi linear.                               │
    │ O(n2)      │ Quadratic complexity.                       │
    │ O(n3)      │ Cubic complexity.                           │
    │ O(n!)      │ Factorial complexity.                       │
    
    >>> TimeProfile(solution, [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000])

    №      Время  Замедление        Число         Результат
    ---  ---------  ------------  ---------  ----------------
     1  0.0008448  0.084%            10000          23331668
     2  0.0084711  0.763%           100000        2333316668
     3  0.095528   8.706%          1000000      233333166668
     4  0.9545     85.897%        10000000    23333331666668
     5  9.6361     868.160%      100000000  2333333316666668
    """
    _last_time = 0
    _timer_has_run_FLAG = False
    timer = ParallelTimer()

    def __init__(self, function, args_list: list = [], DynamicPrint=False, DynamicTimer=False):
        self.function = function
        self.args_list = args_list
        self.DynamicPrintStatFlag = DynamicPrint
        self.DynamicTimerFlag = DynamicTimer
        self.run()

    def run(self):
        result_stats = []
        try:
            if self.DynamicTimerFlag:
                self.timer.start_parallel_timer()

            if self.args_list:

                for arg in self.args_list:
                    result_stats.append(
                        self._get_stats(self.function, arg=arg)
                    )
                    if self.DynamicPrintStatFlag:
                        self.dynamic_print_stats(result_stats)
            else:
                result_stats.append(
                    self._get_stats(self.function, arg=None)
                )

        except KeyboardInterrupt:
            print('\033[91m', 'Программа остановлена.', '\033[0m', end='\n\n')
            pass

        finally:
            if self.DynamicTimerFlag:
                self.timer.stop_parallel_timer()

            if result_stats:
                if len(result_stats) > 1:
                    result_stats = self.numerate_data(result_stats)

                if self.DynamicPrintStatFlag:
                    pass
                else:
                    self.print_stats(result_stats)

    @staticmethod
    def print_stats(data):
        """Arg: data (list of dicts)"""
        print(tabulate(data, headers='keys'))

    @classmethod
    def dynamic_print_stats(cls, data):  # FIXME (работает только в терминале)
        """Arg: data (list of dicts)"""
        os.system('cls' if os.name == 'nt' else 'clear')
        cls.print_stats(data)

    def _get_stats(self, function, arg=None) -> dict:
        """
        Возвращает статистику по запуску функуии
        """
        t = timer()
        if arg != None:
            result = function(arg)
        else:
            result = function()
        time = timer() - t
        slowdown = f"{time - self._last_time:.3%}"
        self._last_time = time
        return {"Время": time, "Замедление": slowdown, "Аргумент": arg,  "Результат": result}

    @staticmethod
    def numerate_data(data):
        """
        Нумерует словари
        Arg: data (list of dicts)
        """
        for index, d in enumerate(data):
            data[index] = {'№': index+1, **d}
        return data


if __name__ == '__main__':
    #~~~~~~~~~~~~~~~~~~~~| Test TimeProfile |#~~~~~~~~~~~~~~~~~~~~#
    def slow_func(number):
        time.sleep(0.05)
        return int(number*math.pi)
    TimeProfile(slow_func, [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000], DynamicTimer=True)

    #~~~~~~~~~~~~~~~~~~~~| Test  ParallelTimer |#~~~~~~~~~~~~~~~~~~~~#
    with ParallelTimer() as ptimer:
        for i in range(5):
            time.sleep(0.05)
