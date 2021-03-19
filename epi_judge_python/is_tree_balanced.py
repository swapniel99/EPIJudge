from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def balanced_binary_tree_helper(node: BinaryTreeNode) -> (bool, int):
    if node is None:
        return True, 0

    leftb, lefth = balanced_binary_tree_helper(node.left)
    rightb, righth = balanced_binary_tree_helper(node.right)

    return leftb and rightb and abs(lefth - righth) <= 1, max(lefth, righth) + 1


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return balanced_binary_tree_helper(tree)[0]


if __name__ == '__main__':
    exit(generic_test.generic_test_main('is_tree_balanced.py', 'is_tree_balanced.tsv', is_balanced_binary_tree))
