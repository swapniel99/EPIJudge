from list_node import ListNode, make_list


def reverseList(head: ListNode):
    if head is None:
        return head

    dummy = ListNode(0, head)

    prev = dummy
    ptr = dummy.next
    while ptr.next is not None:
        temp = ptr.next
        ptr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next


def main():
    l = [5, 23, 5, 23, 53, 3]
    L = make_list(l)

    print(L)
    res = reverseList(L)
    print(res)


if __name__ == '__main__':
    main()
