def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def solution(a, b):
    """
    A (int) - GCD(x, y)
    B (int) - LCM(x, y)
    return: x, y
    """
    product_xy = a * b
    combinations_multipliers = []
    for i in range(1, int(product_xy ** (1 / 2)) + 1):
        if product_xy % i == 0:
            combinations_multipliers.append([i, product_xy // i])

    for (m1, m2) in combinations_multipliers:
        # m1, m2 - candidates for x and y respectively,
        if m1 < a or m2 > b:
            continue
        else:
            if gcd(m1, m2) == a:
                return m1, m2
    return -1
