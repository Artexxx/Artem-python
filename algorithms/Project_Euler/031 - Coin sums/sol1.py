"""
В Англии валютой являются фунты стерлингов ? и пенсы p, и в обращении есть восемь монет:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p)

£2 возможно составить следующим образом:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

Сколькими разными способами можно составить £2, используя любое количество монет?


  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.0006933  0.069%            200        73682
  2  0.0010999  0.04%             400      1960497
  3  0.0027495  0.16%             800     86439345
"""
def memoize(f):
    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)
            # print(f"[#] F(",int(*args), ')\t => \t', dict(cache[args])) # TEST OUTPUT
        return cache[args]
    return wrapper


def solution(amount=200, S=[1, 2, 5, 10, 20, 50, 100, 200]):
    """
    Возращает сколькими разными способами можно составить £2, используя N монет вида S.

    >>> solution(1)
    1
    >>> solution(200)
    73682
    """
    @memoize
    def C(n, m):
        if n < 0 or m <= 0:
            return 0
        if n == 0:
            return 1
        return C(n, m - 1) + C(n - S[m - 1], m)

    return C(amount, len(S))

if __name__ == '__main__':
    print(solution(int(input().strip())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    #
    # my_time_this(solution, [200, 400, 800, 1000])