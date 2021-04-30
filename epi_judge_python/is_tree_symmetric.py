from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def symmetric_helper(node1: BinaryTreeNode, node2: BinaryTreeNode) -> bool:
    return (node1 is None and node2 is None) \
           or (node1 is not None and node2 is not None and node1.data == node2.data
               and symmetric_helper(node1.left, node2.right) and symmetric_helper(node1.right, node2.left))


def is_symmetric(tree: BinaryTreeNode) -> bool:
    return tree is None or symmetric_helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('is_tree_symmetric.py', 'is_tree_symmetric.tsv', is_symmetric))
