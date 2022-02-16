# [Максимум функции Эйлера](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/69.html)

>
> Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения количества чисел, меньших n, которые взаимно просты с n. 
> К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9)=6.
> 
> <table class="table">
> <tbody><tr>
> <td><b><i>n</i></b></td>
> <td><b>Взаимно простые числа</b></td>
> <td><b>φ(<i>n</i>)</b></td>
> <td><b><i>n</i>/φ(<i>n</i>)</b></td>
> </tr>
> <tr>
> <td>2</td><td>1</td><td>1</td><td>2</td>
> </tr>
> <tr>
> <td>3</td><td>1,2</td><td>2</td><td>1.5</td>
> </tr>
> <tr>
> <td>4</td><td>1,3</td><td>2</td><td>2</td>
> </tr>
> <tr>
> <td>5</td><td>1,2,3,4</td><td>4</td><td>1.25</td>
> </tr>
> <tr>
> <td>6</td><td>1,5</td><td>2</td><td>3</td>
> </tr>
> <tr>
> <td>7</td><td>1,2,3,4,5,6</td><td>6</td><td>1.1666...</td>
> </tr>
> <tr>
> <td>8</td><td>1,3,5,7</td><td>4</td><td>2</td>
> </tr>
> <tr>
> <td>9</td><td>1,2,4,5,7,8</td><td>6</td><td>1.5</td>
> </tr>
> <tr>
> <td>10</td><td>1,3,7,9</td><td>4</td><td>2.5</td>
> </tr>
> </tbody></table>
> 
> Нетрудно заметить, что максимум n/φ(n) наблюдается при n=6, для n ≤ 10.
> Найдите значение n ≤ 1 000 000, при котором значение n/φ(n) максимально.
``` python
solution(10**6)  # => 510510
```

## Нормальное решение (1)
Вычисление φ(n) для произвольного натурального n основывается на мультипликативности функции Эйлера _(для относительно простых чисел a и b φ(a*b) = φ(a)*φ(b))_, выражении для φ(p^n), а также на основной теореме арифметики.
Для произвольного натурального числа значение φ(n) представляется в виде:

<img src="https://s0.wp.com/latex.php?latex=%5Cvarphi(n)=n%5Cprod_%7Bp%5Cmid%20n%7D%5Cleft(1-%5Cfrac%7B1%7D%7Bp%7D%5Cright),%5C;%5C;n%3E1+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt="\varphi(n)=n\prod_{p\mid n}\left(1-\frac{1}{p}\right),\;\;n>1" class="latex">
<br>где p — это различные простые множители n.

**Доказательство:**
<br>Как следует из основной теоремы арифметики, всякое натуральное число n>1 единственным образом представляется в виде:
n=p1<sup>a1</sup>⋅...⋅pk<sup>ak</sup>,
где p1<...<pk - простые числа, a1, ..., ak - натуральные числа
Используя мультипликативность функции Эйлера и выражение для φ(p^k), 

![phi-n.svg](res/phi-n.svg)

<br>Пример вычисления:
<br>У 10 есть простые множители 2 и 5.
<br>φ(10) = 10 * (1 - 1/2) * (1 - 1/5) 
<br>    = (10 * (1 - 1/2)) * (1 - 1/5) 
<br>    = (10 - 10/2) * (1 - 1/5) => (phi -= phi/2)
<br>    = 5 * (1 - 1/5) = 5 - 5/5 => (phi -= phi/5) 
<br>    = 4

```python
def get_totients(limit: int) -> List[int]:
    """
    Calculates a list of totients from 0 to `limit` exclusive, using the
    definition of Euler's product formula.

    >>> get_totients(5)
    [0, 1, 1, 2, 2, 4]
    >>> get_totients(10)
    [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
    """
    phi = list(range(limit + 1))

    for p in range(2, len(phi)):
        if phi[p] == p:  # p is prime
            for i in range(p, limit + 1, p):
                phi[i] -= phi[i] // p
    return phi


def solution(limit=10 ** 6):
    """
    Возвращает значение n ≤ limit, при котором значение n/φ(n) максимально.

    >>> solution(10)
    6
    """
    phi = get_totients(limit)
    return max(range(2, limit + 1), key=(lambda i: i / phi[i]))
```
```text
  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0051274  0.513%             10000         2310
  2  0.0659023  6.077%            100000        30030
  3  0.9291     86.320%          1000000       510510
```

## Нормальное решение (2)

<img src="https://s0.wp.com/latex.php?latex=\frac{n}{\phi(n)} = \frac{n}{n \displaystyle\prod_{p | n} \left(1 - \frac{1}{p} \right)} = \frac{1}{\displaystyle\prod_{p | n} \left(1 - \frac{1}{p} \right)} = \prod_{p | n} \frac{p}{p - 1},%5C;%5C;n%3E1+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt="\frac{n}{\phi(n)} = \frac{n}{n \displaystyle\prod_{p | n} \left(1 - \frac{1}{p} \right)} = \frac{1}{\displaystyle\prod_{p | n} \left(1 - \frac{1}{p} \right)} = \prod_{p | n} \frac{p}{p - 1}" class="latex">

Надо максимизировать отношение n/φ(n).
<br>φ(n) уменьшается по мере увеличения p, поэтому учитывая два значения n с равным количеством простых множителей, предпочтительней иметь меньшие простые множители, чем большие.
<br> Число n <= N, минимизирующее φ(n), является наибольшим «простым факториалом», меньшим или равным N.
<br>То есть, чтобы свести отношение n/φ(n) к максимуму, нужно минимизировать знаменатель. 
Каждый раз, когда добавляем отдельный простой множитель, знаменатель становится меньше. 
Поэтому надо искать число с максимальным количеством различных простых множителей.

```python
def bit_sieve(limit: int) -> bytearray:
    """
    Sieve of Eratosthenes
    Input limit>=3, return boolean array of length `limit`,
    where index is number and boolean values is whether prime or not
    The time complexity of this algorithm is O(nloglog(n).

    Example
    ========
    >>> list(bit_sieve(10))
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]

    Time-Profile
    ============
    ===  =========  ============  ===========  ============
      №       Time  Slowdown         Argument  Count primes
    ===  =========  ============  ===========  ============
      1  0.001174   0.118%            100_000          9592
      2  0.013186   1.201%          1_000_000         78498
      3  0.131736   11.855%        10_000_000        664579
      4  1.63013    149.840%      100_000_000       5761455
    ===  =========  ============  ===========  ============
    """
    sieve = bytearray([True]) * limit
    sieve[0] = False
    sieve[1] = False
    # old code ─ slow version
    # number_of_multiples = len(sieve[4::2])
    number_of_multiples = (limit - 4 + limit % 2) // 2
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            # old code ─ slow version
            # number_of_multiples = len(sieve[factor * factor::2*factor])
            number_of_multiples = ((limit - factor * factor - 1) // (2 * factor) + 1)
            sieve[factor * factor::factor * 2] = [False] * number_of_multiples
    return sieve


def prime_sieve(limit) -> Iterator[int]:
    sieve = bit_sieve(limit+1)
    yield 2
    yield from (i for i in range(3, limit+1, 2) if sieve[i])


def solution(limit=10 ** 6):
    """
    Возвращает значение n ≤ limit, при котором значение n/φ(n) максимально.
    """

    result = 1
    for prime in prime_sieve(isqrt(limit)):
        result *= prime
        if result * prime >= limit:
            return result
```
```text
  №     Время  Замедление      Аргумент    Результат
---  --------  ------------  ----------  -----------
  1  1.35e-05  0.001%             10000         2310
  2  1.07e-05  -0.000%           100000        30030
  3  1.51e-05  0.000%           1000000       510510
```