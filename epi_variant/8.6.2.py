from binary_tree_node import BinaryTreeNode
from collections import deque


def reverseLevelOrder(root: BinaryTreeNode):
    res = list()
    q = deque()
    q.append((root, 0))

    cur_depth = 0
    temp = list()
    while q:
        node, depth = q.popleft()

        if node is None:
            continue

        q.append((node.left, depth + 1))
        q.append((node.right, depth + 1))

        if depth > cur_depth:
            res.append(temp)
            cur_depth = depth
            temp = list()

        temp.append(node.val)

    if temp:
        res.append(temp)

    res.reverse()

    return res
