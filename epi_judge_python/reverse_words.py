import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reverse_range(s, i, j):
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    s.reverse()

    i = j = 0
    while j < len(s):
        if s[j] == ' ':
            reverse_range(s, i, j - 1)
            i = j = j + 1
        else:
            j += 1
    reverse_range(s, i, j - 1)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv', reverse_words_wrapper))
