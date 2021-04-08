from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def rev_dfs(node, k, res):
    if node is not None and len(res) < k:
        rev_dfs(node.right, k, res)
        if len(res) < k:
            res.append(node.data)
        rev_dfs(node.left, k, res)


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    res = list()
    rev_dfs(tree, k, res)
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('k_largest_values_in_bst.py', 'k_largest_values_in_bst.tsv',
                                        find_k_largest_in_bst, test_utils.unordered_compare))
