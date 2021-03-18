from binary_tree_node import BinaryTreeNode
from collections import deque


def avgLevel(root: BinaryTreeNode):
    res = list()
    q = deque()
    q.append((root, 0))

    cur_depth = 0
    sum = 0
    count = 0
    while q:
        node, depth = q.popleft()

        if node is None:
            continue

        q.append((node.left, depth + 1))
        q.append((node.right, depth + 1))

        if depth > cur_depth:
            res.append(sum / count)
            sum = 0
            count = 0
            cur_depth = depth

        sum += node.val
        count += 1

    if count:
        res.append(sum / count)

    return res
