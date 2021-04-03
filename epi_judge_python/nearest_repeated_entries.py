from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    last_index = dict()
    res = float('inf')
    for i, s in enumerate(paragraph):
        if s in last_index:
            res = min(res, i - last_index[s])
        last_index[s] = i
    return res if res != float('inf') else -1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('nearest_repeated_entries.py', 'nearest_repeated_entries.tsv',
                                        find_nearest_repetition))
