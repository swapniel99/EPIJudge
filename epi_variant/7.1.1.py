from doubly_list_node import DoublyListNode, make_list


def merge_two_sorted_lists(L1: DoublyListNode, L2: DoublyListNode) -> DoublyListNode:
    ptr1 = L1
    ptr2 = L2
    dummy = DoublyListNode()
    ptr = dummy

    while ptr1 is not None and ptr2 is not None:
        if ptr1.data < ptr2.data:
            ptr.next = ptr1
            ptr1.prev = ptr
            ptr1 = ptr1.next
        else:
            ptr.next = ptr2
            ptr2.prev = ptr
            ptr2 = ptr2.next
        ptr = ptr.next

    rem = ptr1 or ptr2
    ptr.next = rem
    rem.prev = ptr

    return dummy.next


def main():
    l1 = [2, 5, 6, 9]
    l2 = [1, 3, 4, 7, 10, 20]

    L1 = make_list(l1)
    L2 = make_list(l2)

    print(L1)
    print(L2)

    res = merge_two_sorted_lists(L1, L2)
    print(res)


if __name__ == '__main__':
    main()
