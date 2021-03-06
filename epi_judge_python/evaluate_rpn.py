from test_framework import generic_test

import operator


def evaluate(expression: str) -> int:
    operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    expression = expression.split(',')
    stack = list()

    for e in expression:
        if e in operator_dict:
            b = stack.pop()
            a = stack.pop()
            stack.append(operator_dict[e](a, b))
        else:
            stack.append(int(e))

    return stack[-1]


if __name__ == '__main__':
    exit(generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv', evaluate))
