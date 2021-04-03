import heapq


def kth_largest_stable(A, k):
    minheap = [(A[i], i) for i in range(k)]
    heapq.heapify(minheap)

    for i in range(k, len(A)):
        heapq.heappush(minheap, (A[i], i))
        heapq.heappop(minheap)

    return minheap[0][0]


class Elem(object):
    def __init__(self, val, extra):
        self.val = val
        self.extra = extra

    def __repr__(self):
        return str((self.val, self.extra))

    def __str__(self):
        return repr(self)

    def __lt__(self, other):
        return self.val < other.val


def main():
    A = [Elem(5, 6), Elem(7, 3), Elem(5, 4), Elem(2, 5), Elem(9, 4), Elem(7, 1)]
    k = 2

    print(kth_largest_stable(A, k))
    print(sorted(A))


if __name__ == '__main__':
    main()
