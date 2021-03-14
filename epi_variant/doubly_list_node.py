class DoublyListNode:
    def __init__(self, data=0, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __eq__(self, other):
        if self.prev is not None or other.prev is not None:
            return False
        a, b = self, other
        while a and b:
            if a.data != b.data:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    def __repr__(self):
        node = self
        visited = set()
        first = True

        result = ''

        while node:
            if first:
                first = False
            else:
                result += ' <-> '

            if id(node) in visited:
                if node.next is not node:
                    result += str(node.data)
                    result += ' <-> ... <-> '

                result += str(node.data)
                result += ' <-> ...'
                break
            else:
                result += str(node.data)
                visited.add(id(node))
            node = node.next

        return result

    def __str__(self):
        return self.__repr__()


def list_size(node):
    result = 0
    visited = set()

    while node is not None and id(node) not in visited:
        result += 1
        visited.add(id(node))
        node = node.next

    return result


def make_list(L):
    dummy = DoublyListNode()
    ptr = dummy
    for n in L:
        node = DoublyListNode(n)
        ptr.next = node
        node.prev = ptr
        ptr = ptr.next

    res = dummy.next
    res.prev = None

    return res
