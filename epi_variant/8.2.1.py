import operator


def evaluate(expression: str) -> int:
    operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    expression = expression.split(',')
    expression.reverse()
    stack = list()

    for e in expression:
        if e in operator_dict:
            a = stack.pop()
            b = stack.pop()
            stack.append(operator_dict[e](a, b))
        else:
            stack.append(int(e))

    return stack[-1]


print(evaluate('*,+,1,3,-,2,3'))
