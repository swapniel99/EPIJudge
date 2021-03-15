from list_node import ListNode, make_list


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)

    prevtail = dummy
    while True:
        temp = prevtail
        for _ in range(k):
            temp = temp.next
            if temp is None:
                return dummy.next

        tail = prevtail.next
        for _ in range(k - 1):
            temp = tail.next
            tail.next = temp.next
            temp.next = prevtail.next
            prevtail.next = temp
        prevtail = tail


def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    L = make_list(l)

    print(L)
    res = reverseKGroup(L, 3)
    print(res)


if __name__ == '__main__':
    main()
