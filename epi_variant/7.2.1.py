from list_node import ListNode, make_list


def reverseList(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)

    ptr = dummy.next
    while ptr and ptr.next:
        temp = ptr.next
        ptr.next = temp.next
        temp.next = dummy.next
        dummy.next = temp

    return dummy.next


def main():
    l = [1, 2, 3, 4, 5, 6]
    L = make_list(l)

    print(L)
    res = reverseList(L)
    print(res)


if __name__ == '__main__':
    main()
