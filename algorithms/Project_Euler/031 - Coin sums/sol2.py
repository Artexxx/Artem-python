"""
В Англии валютой являются фунты стерлингов ? и пенсы p, и в обращении есть восемь монет:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p)

£2 возможно составить следующим образом:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

Сколькими разными способами можно составить £2, используя любое количество монет?
"""


def solution(n=200, coins=[1, 2, 5, 10, 20, 50, 100, 200]):
    """
    Возращает сколькими разными способами можно составить £2, используя N монет вида S

    >>> solution(1)
    1
    >>> solution(200)
    73682
    """
    ways = [1] + [0] * n
    print(ways)

    for coin in coins:
        for i in range(coin, n + 1):
            ways[i] += ways[i - coin]
        print(ways)
    return ways[n]


if __name__ == "__main__":
    print(solution())
