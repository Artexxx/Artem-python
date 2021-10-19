"""
Степени, равные количеству цифр
Пятизначное число 16807 = 7^5 является также пятой степенью натурального числа.
Аналогично, девятизначное число 134217728 = 8^9 является девятой степенью.

Сколько существует n-значных натуральных чисел, являющихся также и n-ми степенями натуральных чисел?

    Время  Замедление   Результат
---------  ------------ ---------
0.0006391  0.064%              49
"""


def solution():
    """
    Находит количество n-значных натуральных чисел, являющихся также и n-ми степенями натуральных чисел
    """
    result_count = 0

    for exp in range(1, 22):
        base = 1
        digit_count = 1
        while digit_count <= exp:
            powerful = base ** exp
            digit_count = len(str(powerful))

            if digit_count == exp:
                result_count += 1

            base += 1

    return result_count


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile;
    TimeProfile(solution)