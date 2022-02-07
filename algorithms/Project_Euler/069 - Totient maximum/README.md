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
solution()  # => 
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

<br>Пример вычисления: φ(36)=φ(2<sup>2</sup> ⋅ 3<sup>2</sup>)=φ(2<sup>2</sup>)φ(3<sup>2</sup>)=(2<sup>2</sup>-2)(3<sup>2</sup>-3)=2⋅6=12

```python
def solution(limit=10 ** 6):
    """
    Возвращает значение n ≤ limit, при котором значение n/φ(n) максимально.
    """
    phi = list(range(limit + 1))

    for p in range(2, len(phi)):
        if phi[p] == p:  # p is prime
            for i in range(2 * p, limit + 1, p):
                phi[i] -= phi[i] // p

    return max(range(2, limit + 1),
               key=(lambda i: i / phi[i]))
```
```text
  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0051274  0.513%             10000         2310
  2  0.0659023  6.077%            100000        30030
  3  0.9291     86.320%          1000000       510510
```

## Нормальное решение (2)

Так как φ мультипликативна и для простого p: φ(p^n) = p^(n-1)*(p-1).
Следовательно, φ(n) = n / φ (n), очевидно, также мультипликативно с φ(p^n) = p/(p-1). 

<img src="https://s0.wp.com/latex.php?latex=\frac{n}{\phi(n)} = \frac{n}{n \displaystyle\prod_{p | n} \left(1 - \frac{1}{p} \right)} = \frac{1}{\displaystyle\prod_{p | n} \left(1 - \frac{1}{p} \right)} = \prod_{p | n} \frac{p}{p - 1},%5C;%5C;n%3E1+&amp;bg=ffffff&amp;fg=000&amp;s=0" alt="\frac{n}{\phi(n)} = \frac{n}{n \displaystyle\prod_{p | n} \left(1 - \frac{1}{p} \right)} = \frac{1}{\displaystyle\prod_{p | n} \left(1 - \frac{1}{p} \right)} = \prod_{p | n} \frac{p}{p - 1}" class="latex">

Поэтому для максимизации φ(n) нет смысла смотреть на значения n, содержащие простые числа в степени больше 1: не надо менять значение φ(n), а просто увеличиваете n.
Более того, φ(p) уменьшается по мере увеличения p, поэтому учитывая два значения n с равным числом простых множителей, предпочтительней иметь меньшие простые множители, чем большие.
Из этого следует, что n <= N, максимизирующий φ(n), является наибольшим «простым факториалом», меньшим или равным N.

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
    zero = bytearray([False])

    sieve[0] = False
    sieve[1] = False
    number_of_multiples = len(sieve[4::2])
    sieve[4::2] = [False] * number_of_multiples

    for factor in range(3, int(math.sqrt(limit)) + 1, 2):
        if sieve[factor]:
            # number_of_multiples = len(sieve[factor * factor::2*factor]) # old code ─ slow version
            number_of_multiples = ((limit - factor * factor - 1) // (2 * factor) + 1)
            sieve[factor * factor::factor * 2] = zero * number_of_multiples
    return sieve


def prime_sieve(limit) -> Iterator[int]:
    sieve = bit_sieve(limit)
    yield 2
    yield from (i for i in range(3, limit, 2) if sieve[i])


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