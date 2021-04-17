from typing import Set

from test_framework import generic_test

from string import ascii_lowercase as alphabet
from collections import deque


def transform_string(D: Set[str], s: str, t: str) -> int:
    if s not in D or t not in D:
        return -1
    if s == t:
        return 0

    visited = set()
    q = deque()
    q.append((s, 0))
    while q:
        cur_s, depth = q.popleft()
        if cur_s == t:
            return depth
        visited.add(cur_s)
        temp = list(cur_s)
        for i in range(len(cur_s)):
            old_c = temp[i]
            for c in alphabet:
                if c == old_c:
                    continue
                temp[i] = c
                new_s = ''.join(temp)
                if new_s in D and new_s not in visited:
                    q.append((new_s, depth + 1))
            temp[i] = old_c
    return -1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('string_transformability.py', 'string_transformability.tsv', transform_string))
