from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    res = list()
    q = deque()

    q.append((tree, 0))

    cur_depth = 0
    temp = list()
    while q:
        node, depth = q.popleft()

        if node is None:
            continue

        q.append((node.left, depth+1))
        q.append((node.right, depth+1))

        if depth > cur_depth:
            res.append(temp)
            cur_depth = depth
            temp = list()

        temp.append(node.data)

    if temp:
        res.append(temp)

    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('tree_level_order.py', 'tree_level_order.tsv', binary_tree_depth_order))
