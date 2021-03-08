import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Time O(n), Space O(1)
def replace_and_remove(size: int, s: List[str]) -> int:
    ca = 0
    cb = 0
    for c in s:
        if c == 'a':
            ca += 1
        elif c == 'b':
            cb += 1
    final_len = size + ca - cb

    reader = size - 1
    writer = -1

    while reader >= 0:
        if s[reader] == 'a':
            s[writer] = 'd'
            s[writer-1] = 'd'
            writer -= 2
        elif s[reader] != 'b':
            s[writer] = s[reader]
            writer -= 1
        reader -= 1

    for i in range(final_len):
        s[i] = s[-final_len + i]

    return final_len


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(generic_test.generic_test_main('replace_and_remove.py', 'replace_and_remove.tsv', replace_and_remove_wrapper))
