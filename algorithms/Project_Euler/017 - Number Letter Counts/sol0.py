import inflect
p = inflect.engine()

print(sum(len(p.number_to_words(n).replace('-', '').replace(' ', '')) for n in range(1, 1001)))