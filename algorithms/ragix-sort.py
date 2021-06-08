def radix_sort(lst):
    RADIX = 10
    placement = 1

    # get the maximum number
    max_digit = max(lst)

    while placement < max_digit:
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split lst between lists
        for i in lst:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)

        # empty lists into lst array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                lst[a] = i
                a += 1

        # move to next
        placement *= RADIX


def radix_sort(arr, radix=10):
    max_length = False
    tmp, digit = -1, 1

    while not max_length:
        max_length = True
        # declare and initialize buckets
        buckets = [[] for _ in range(radix)]

        # split arr between lists
        for i in arr:
            tmp = i // digit
            buckets[tmp % radix].append(i)
            if max_length and tmp > 0:
                max_length = False

        # empty lists into arr array
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1

        # move to next digit
        digit *= radix
    return arr


test = [170, 45, 75, 90, 802, 24, 2, 66]

print('Sorted array:', radix_sorted(test))
