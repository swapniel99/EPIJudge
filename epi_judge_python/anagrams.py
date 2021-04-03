from typing import List

from test_framework import generic_test, test_utils

from collections import defaultdict
from string import ascii_lowercase


def digest(s):
    ctr = [0] * 26
    for c in s:
        if c in ascii_lowercase:
            ctr[ord(c) - ord('a')] += 1
    return tuple(ctr)


# O(n * m) n is number of strings, and m is max length of any string
def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in dictionary:
        res[digest(s)].append(s)

    return [group for group in res.values() if len(group) > 1]


if __name__ == '__main__':
    exit(generic_test.generic_test_main('anagrams.py', 'anagrams.tsv', find_anagrams,
                                        comparator=test_utils.unordered_compare))
