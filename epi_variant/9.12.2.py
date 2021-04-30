from typing import List

from binary_tree_node import BinaryTreeNode


def max_tree_helper(array: List, start: int, end: int) -> BinaryTreeNode:
    if end <= start:
        return None
    else:
        max_n = array[start]
        max_i = start
        for i in range(start + 1, end):
            if array[i] > max_n:
                max_n = array[i]
                max_i = i
        node = BinaryTreeNode(max_n)
        node.left = max_tree_helper(array, start, max_i)
        node.right = max_tree_helper(array, max_i + 1, end)
        return node


def max_tree(array: List) -> BinaryTreeNode:
    return max_tree_helper(array, 0, len(array))


array = [2, 4, 1, 55, 3, 5, 6, 7, 4]

print(max_tree(array))
