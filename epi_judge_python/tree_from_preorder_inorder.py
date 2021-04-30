from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def tree_helper(preorder, inorder, order, pstart, pend, istart, iend):
    if pend <= pstart:
        return None
    else:
        val = preorder[pstart]
        node = BinaryTreeNode(val)
        inorder_index = order[val]
        leftlen = inorder_index - istart
        node.left = tree_helper(preorder, inorder, order, pstart + 1, pstart + leftlen + 1, istart, inorder_index)
        node.right = tree_helper(preorder, inorder, order, pstart + leftlen + 1, pend, inorder_index + 1, iend)
        return node


def binary_tree_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> BinaryTreeNode:
    order = {n: i for i, n in enumerate(inorder)}
    return tree_helper(preorder, inorder, order, 0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(generic_test.generic_test_main('tree_from_preorder_inorder.py', 'tree_from_preorder_inorder.tsv',
                                        binary_tree_from_preorder_inorder))
