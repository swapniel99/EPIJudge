import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    p0, p1 = l0, l1

    while p0 and p1:
        p0, p1 = p0.next, p1.next

    if p0 is None:
        l0, l1 = l1, l0

    rem = p0 or p1
    while rem:
        rem, l0 = rem.next, l0.next

    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next

    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(generic_test.generic_test_main('do_terminated_lists_overlap.py', 'do_terminated_lists_overlap.tsv', overlapping_no_cycle_lists_wrapper))
