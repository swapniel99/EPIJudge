from typing import Iterator, List

from test_framework import generic_test

import heapq


def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    heap = list()
    res = list()
    for n in sequence:
        heapq.heappush(heap, n)
        if len(heap) > k:
            res.append(heapq.heappop(heap))

    while heap:
        res.append(heapq.heappop(heap))

    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
                                        sort_approximately_sorted_array_wrapper))
