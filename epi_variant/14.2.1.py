from typing import Optional
from bst_node import BstNode


def find_first_equal_to_k(tree: BstNode, k: int) -> Optional[BstNode]:
    node = tree
    first_match = None
    while node is not None:
        if node.data == k:
            first_match = node
        if node.data >= k:
            node = node.left
        else:
            node = node.right
    return first_match
