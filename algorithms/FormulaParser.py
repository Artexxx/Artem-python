"""
FormulaParser -- переобразует выражение из инфиксной формы в постфиксную и вычисляет

>>> evaluate('3+4*2/(1-5)^8')
>>> 3.0
"""

OPERATORS = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x / y),
}


def parse(formula: str):
    number = ""
    for s in formula:
        if s.isdecimal():
            number += s
        elif number:
            yield float(number)
            number = ""
        if s in OPERATORS or s in "()":
            yield s
    if number:
        yield float(number)


def translate_in_postfix(parsed_formula):
    stack = []
    for token in parsed_formula:
        if token in OPERATORS:
            while (stack and stack[-1] != "("
                   and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]):
                yield stack.pop()
            stack.append(token)
        elif token == ")":
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                yield x
        elif token == "(":
            stack.append(token)
        else:
            yield token
    while stack:
        yield stack.pop()


def calculate(postfix):
    stack = []
    for token in postfix:
        if token in OPERATORS:
            y, x = stack.pop(), stack.pop()
            stack.append(OPERATORS[token][1](x, y))
        else:
            stack.append(token)
    return stack[0]


def evaluate(formula: str):
    return calculate(translate_in_postfix(parse(formula)))


if __name__ == '__main__':
    print(evaluate("2+5"))
