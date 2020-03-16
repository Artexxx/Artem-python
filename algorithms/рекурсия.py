def factorial(num):
    if num == 0:  # Базовый  случай
        return 1
    return factorial(num - 1) * num


# Сумма цифр числа
def sum_n(num):
    if num:
        return num % 10 + sum_n(num // 10)
    return 0


# Сумма массива
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


# Цифры числа справа налево
def reverse_n(n):
    if (n < 10):
        return n
    else:
        print(n % 10)
    return reverse_n(n // 10)


# Цифры числа слева направо
def lToR(n):
    if n == 0:
        return
    else:
        lToR(n // 10)
        print(n % 10, end=' ')
