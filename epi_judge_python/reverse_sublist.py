from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy = ListNode(0, L)

    prev = dummy
    for _ in range(start - 1):
        prev = prev.next

    last = prev.next
    for _ in range(start, finish):
        temp = last.next
        last.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next


if __name__ == '__main__':
    exit(generic_test.generic_test_main('reverse_sublist.py', 'reverse_sublist.tsv', reverse_sublist))
