from typing import List

from binary_tree_node import BinaryTreeNode


def tree_helper(postorder, inorder, order, pstart, pend, istart, iend):
    if pend <= pstart:
        return None
    else:
        val = postorder[pend - 1]
        node = BinaryTreeNode(val)
        inorder_index = order[val]
        leftlen = inorder_index - istart
        node.left = tree_helper(postorder, inorder, order, pstart, pstart + leftlen, istart, inorder_index)
        node.right = tree_helper(postorder, inorder, order, pstart + leftlen, pend - 1, inorder_index + 1, iend)
        return node


def binary_tree_from_postorder_inorder(postorder: List[int], inorder: List[int]) -> BinaryTreeNode:
    order = {n: i for i, n in enumerate(inorder)}
    return tree_helper(postorder, inorder, order, 0, len(postorder), 0, len(inorder))


postorder = [9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]

print(binary_tree_from_postorder_inorder(postorder, inorder))
