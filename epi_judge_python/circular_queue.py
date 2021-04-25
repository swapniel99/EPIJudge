from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.head = self.tail = self.len = 0

    def enqueue(self, x: int) -> None:
        if self.len == self.capacity:
            temp = [0] * (2 * self.capacity)
            for i in range(self.len):
                temp[i] = self.arr[(self.head + i) % self.capacity]
            self.arr = temp
            self.capacity *= 2
            self.head = 0
            self.tail = self.len
        self.arr[self.tail] = x
        self.tail = (1 + self.tail) % self.capacity
        self.len += 1

    def dequeue(self) -> int:
        res = self.arr[self.head]
        self.head = (1 + self.head) % self.capacity
        self.len -= 1
        return res

    def size(self) -> int:
        return self.len


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' + str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('circular_queue.py', 'circular_queue.tsv', queue_tester))
