def gcd(a, b):
    """Computes the greatest common divisor of the integers a and b"""
    while b: a, b = b, a % b
    return abs(a)
