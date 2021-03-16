from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.arr = list()
        self.max_arr = list()

    def empty(self) -> bool:
        return not bool(self.arr)

    def max(self) -> int:
        return self.max_arr[-1]

    def pop(self) -> int:
        res = self.arr.pop()
        if res == self.max():
            self.max_arr.pop()
        return res

    def push(self, x: int) -> None:
        if self.empty() or x >= self.max():
            self.max_arr.append(x)
        self.arr.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(generic_test.generic_test_main('stack_with_max.py', 'stack_with_max.tsv', stack_tester))
