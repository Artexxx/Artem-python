"""
Каждое n-значное число, которое содержит каждую цифру от 1 до n ровно один раз, будем считать пан-цифровым;
  к примеру, 5-значное число 15234 является пан-цифровым, т.к. содержит цифры от 1 до 5.
Произведение 7254 является необычным, поскольку равенство 39 × 186 = 7254, состоящее из
 множимого, множителя и произведения является пан-цифровым, т.е. содержит цифры от 1 до 9.
Найдите сумму всех пан-цифровых произведений, для которых равенство "множимое × множитель = произведение"
 можно записать цифрами от 1 до 9, используя каждую цифру только один раз.

Примечание: Некоторые произведения можно получить несколькими способами, поэтому убедитесь, что включили их в сумму лишь единожды.
"""


def distinct(str_abc):
    set_s = set(str_abc)
    return len(str_abc) == len(set_s) and not ('0' in set_s)


def pandigital_products_sum() -> int:
    """
    Возращает сумму всех пан-цифровых произведений.

    >>> solution()
    45228
    """
    result_set = set()
    for a in range(2, 1000):
        if not distinct(str(a)): continue
        for b in range(a + 1, 25000):
            c = a * b
            str_abc = f'{a}{b}{c}'
            if len(str_abc) > 9:
                break
            if len(str_abc) == 9 and distinct(str_abc):
                result_set.add(c)
    return sum(result_set)


if __name__ == '__main__':
    print(pandigital_products_sum())