n = int(input())
h = [int(x) for x in input().split()]

ps0 = [0] * (n + 1)
for i in range(n):
    ps0[i + 1] = ps0[i] + h[i]

bb = [n] * (n + 3)
bh = [0] * (n + 3)
ps = [0] * (n + 3)

m = 1
bb[0] = 0
bh[0] = h[0]

INF = 4 * 10 ^ 9


def ceildiv(a, b):
    return (a - 1) // b + 1


def find_block(i):
    if i < 0:
        return -1
    left = 0
    right = m
    while right - left > 1:
        mid = (left + right) // 2
        if bb[mid] <= i:
            left = mid
        else:
            right = mid
    return left


def get_h(i):
    if i < 0:
        return INF
    return bh[find_block(i)]


def sum_all(left, right):
    bl = find_block(left)
    return ps0[right] - (ps[bl] + bh[bl] * (left - bb[bl]))


for i in range(1, n):
    left = 0
    right = i + 1
    while right - left > 1:
        mid = (left + right) // 2
        if ceildiv(h[i] + sum_all(mid, i), i - mid + 1) <= get_h(mid - 1):
            left = mid
        else:
            right = mid
    m = find_block(left - 1) + 1
    hl = get_h(left - 1)
    s = h[i] + sum_all(left, i)
    hm = ceildiv(s, i - left + 1)
    if hm != hl:
        bb[m] = left
        bh[m] = hm
        ps[m] = ps[m - 1] + (bb[m] - bb[m - 1]) * bh[m - 1]
        m += 1
    if s % (i - left + 1):
        bb[m] = left + s % (i - left + 1)
        bh[m] = hm - 1
        ps[m] = ps[m - 1] + (bb[m] - bb[m - 1]) * bh[m - 1]
        m += 1

bb[m] = n
ans = []
for i in range(m):
    for j in range(bb[i + 1] - bb[i]):
        ans.append(bh[i])
print(*ans)
