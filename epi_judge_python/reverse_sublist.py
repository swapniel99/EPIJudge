from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> ListNode:
    if start == finish:
        return L

    dummy = ListNode(0, L)

    prev = dummy
    for _ in range(start - 1):
        prev = prev.next

    ptr0 = prev
    ptr1 = ptr0.next
    for _ in range(start, finish + 1):
        temp = ptr1.next
        ptr1.next = ptr0
        ptr0, ptr1 = ptr1, temp

    prev.next.next = ptr1
    prev.next = ptr0

    return dummy.next


if __name__ == '__main__':
    exit(generic_test.generic_test_main('reverse_sublist.py', 'reverse_sublist.tsv', reverse_sublist))
