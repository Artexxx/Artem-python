def solution(N, list):
    i = 1
    while i < N:
        index = i
        need_return = False
        while index > 0 and list[index] > 0 and list[index] > list[index - 1]:
            list[index] -= 1
            list[index - 1] += 1
            need_return = True
            index -= 1
        if need_return:
            i -= 1
        i += 1
    return list

print(solution(10, [2, 1, 6, 8, 1, 2, 1, 3, 5, 4]))
