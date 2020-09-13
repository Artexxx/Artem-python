from itertools import combinations_with_replacement

ex, s = int(input('Exponent? ')), 0
p = {str(i): i ** ex for i in range(10)}

isis = 1
for cx in combinations_with_replacement('0123456789', ex + (ex >= 5)):
    isis += 1
    t = sum(p[x] for x in cx)
    sd = sum(p[x] for x in str(t))
    if t == sd and t > 9: s += t

print("Sum of power digits for exponent", ex, "is", (s if s > 0 else "*NONE*"))
