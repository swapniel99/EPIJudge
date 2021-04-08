from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    node = tree
    firstgt = None
    while node is not None:
        if node.data > k:
            firstgt = node
            node = node.left
        else:
            node = node.right
    return firstgt


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('search_first_greater_value_in_bst.py', 'search_first_greater_value_in_bst.tsv',
                                        find_first_greater_than_k_wrapper))
