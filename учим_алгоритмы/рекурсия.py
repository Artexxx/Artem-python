def factorial(num):
    if num == 0:  # Базовый  случай
        return 1
    return factorial(num - 1) * num


# Сумма цифр числа
def sum_n(a):
    if a:
        return a % 10 + sum_n(a // 10)
    # Базовый  случай
    return 0


# Цифры числа справа налево
def reverse_n(n):
    # Базовый  случай
    if (n < 10):
        return n
    else:
        print(n % 10)
    return reverse_n(n // 10)


# Цифры числа слева направо
def lToR(n):
    # Базовый  случай
    if n == 0:
        return
    else:
        lToR(n // 10)
        print(n % 10, end=' ')
