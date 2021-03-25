import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    ptr0 = node0
    ptr1 = node1

    while ptr0 is not ptr1:
        ptr0 = ptr0.parent
        ptr1 = ptr1.parent
        if ptr0 is None or ptr1 is None:
            break
    else:
        return ptr0

    if ptr1 is None:
        node0, node1 = node1, node0
        ptr0, ptr1 = ptr1, ptr0

    d = 0
    while ptr1 is not None:
        ptr1 = ptr1.parent
        d += 1

    ptr0 = node0
    ptr1 = node1

    for i in range(d):
        ptr1 = ptr1.parent

    while ptr0 is not ptr1:
        ptr0 = ptr0.parent
        ptr1 = ptr1.parent
    else:
        return ptr0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0), must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(generic_test.generic_test_main('lowest_common_ancestor_with_parent.py', 'lowest_common_ancestor.tsv',
                                        lca_wrapper))
