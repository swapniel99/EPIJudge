from typing import List

from test_framework import generic_test

import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    minheap = [(a[0], 0, j) for j, a in enumerate(sorted_arrays) if a]
    heapq.heapify(minheap)
    res = list()

    while minheap:
        e, i, j = heapq.heappop(minheap)
        a = sorted_arrays[j]
        if len(a) > i + 1:
            heapq.heappush(minheap, (a[i + 1], i + 1, j))
        res.append(e)

    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('sorted_arrays_merge.py', 'sorted_arrays_merge.tsv', merge_sorted_arrays))
