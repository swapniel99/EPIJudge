from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: ListNode, L2: ListNode) -> ListNode:
    ptr1 = L1
    ptr2 = L2
    dummy = ListNode()
    ptr = dummy

    while ptr1 is not None and ptr2 is not None:
        if ptr1.data < ptr2.data:
            ptr.next = ptr1
            ptr1 = ptr1.next
        else:
            ptr.next = ptr2
            ptr2 = ptr2.next
        ptr = ptr

    ptr.next = ptr1 or ptr2

    return dummy.next


if __name__ == '__main__':
    exit(generic_test.generic_test_main('sorted_lists_merge.py', 'sorted_lists_merge.tsv', merge_two_sorted_lists))
