import sys
import time
from tabulate import tabulate
from itertools import cycle
from timeit import default_timer as timer
import os


class TimeProfile:
    """
    Оценивает время работы 1 алгоритма

    |------------------------------+-------------------|
    |          Полином             |  Функции          |
    |------------------------------+-------------------|
    | 1.00  log2(N)   +  1.25e-015 | N                 |
    | 2.00  log2(N)   +  5.31e-018 | N*N               |
    | 1.19  log2(N)   +      1.116 | N*log2(N)         |
    | 1.37  log2(N)   +      2.232 | N*log2(N)*log2(N) |

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
    _result_stats = []
    _timer_has_run_FLAG = False
    _timer_is_running = False

    def __init__(self, function, args_list: list = [], DynamicPrintStat=False, DynamicTimer=False):
        self.function = function
        self.args_list = args_list
        self.DynamicPrintStatFlag = DynamicPrintStat
        self.DynamicTimerFlag = DynamicTimer
        self.run()

    def run(self, *args, **kwargs):
        self._result_stats = []
        try:
            if self.DynamicTimerFlag:
                self._start_parrallel_timer()

            if self.args_list:

                for arg in self.args_list:
                    self._result_stats.append(
                        self._get_stats(self.function, arg=arg)
                    )
                    if self.DynamicPrintStatFlag:
                        self._dynamic_print_stats(self._result_stats)
            else:
                self._result_stats.append(
                    self._get_stats(self.function, arg=None)
                )

        except KeyboardInterrupt:
            print('\033[91m', 'Программа остановлена.', '\033[0m', end='\n\n')
            pass

        finally:
            if self.DynamicTimerFlag:
                self._stop_parrallel_timer()

            if self._result_stats:
                if self.DynamicPrintStatFlag:
                    pass
                else:
                    self._print_stats(self._result_stats)

    def _print_stats(self, data):
        print(tabulate(data, headers=["Время", "Замедление", "Число", "Результат"]))

    def _dynamic_print_stats(self, data):  # FIXME (работает только в терминале)
        os.system('cls' if os.name == 'nt' else 'clear')
        self._print_stats(data)

    def _get_stats(self, function, arg=None) -> list:
        """
        Возвращает статистику по запуску функуии

        return: ["Время работы":, "Замедление", "Аргумент", "Результат"]
        """
        t = timer()
        if arg:
            result = function(arg)
        else:
            result = function()
        time = timer() - t

        slowdown = f"{time - self._last_time:.3%}"
        self._last_time = time
        return [time, slowdown, arg, result]

    def _start_parrallel_timer(self):
        self._timer_has_run_FLAG = True
        self._timer_is_running = True

        import threading
        self.parrallel_timer_task = threading.Thread(target=self._parrallel_timer)
        self.parrallel_timer_task.start()

    def _stop_parrallel_timer(self):  # FIXME
        self._timer_has_run_FLAG = False
        self.parrallel_timer_task.join()

        while self._timer_is_running:
            time.sleep(0.1)

        return 1

    def _parrallel_timer(self):
        t = timer()
        self._timer_time = 0.0
        phases = cycle(['◑', '◒', '◐', '◓'])

        while self._timer_has_run_FLAG:
            sys.stdout.write(f"\rВремя работы {next(phases)} {self._timer_time:.4}s")
            sys.stdout.flush()
            time.sleep(0.05)
            self._timer_time = timer() - t

        self._timer_is_running = False
        print(f"\rТаймер закончил работу, время = {self._timer_time:.3}s", end='\n\n')
        return 1


if __name__ == '__main__':
    import time

    def slow_func(number):
        time.sleep(1.1123123123)
        return number**3

    TimeProfile(slow_func, [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000], DynamicTimer=True)