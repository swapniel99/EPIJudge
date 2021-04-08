from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# Time O(n), Space O(h)
# def is_binary_tree_bst_helper(tree):
#     if tree is None:
#         return True, float('inf'), float('-inf')
#
#     leftres, leftmin, leftmax = is_binary_tree_bst_helper(tree.left)
#     rightres, rightmin, rightmax = is_binary_tree_bst_helper(tree.right)
#
#     return leftres and rightres and leftmax <= tree.data <= rightmin, min(tree.data, leftmin, rightmin),\
#            max(tree.data, leftmax, rightmax)


# Time O(n), Space O(h)
def is_binary_tree_bst_helper(tree, low, high):
    if tree is None:
        return True
    elif not low <= tree.data <= high:
        return False
    else:
        return is_binary_tree_bst_helper(tree.left, low, tree.data)\
               and is_binary_tree_bst_helper(tree.right, tree.data, high)


# Time O(n), Space O(n)
# def is_binary_tree_bst_helper(tree):
#     from collections import deque
#     q = deque()
#     q.append((tree, float('-inf'), float('inf')))
#
#     while q:
#         node, low, high = q.popleft()
#         if node is not None:
#             if not low <= node.data <= high:
#                 return False
#             q.append((node.left, low, node.data))
#             q.append((node.right, node.data, high))
#
#     return True


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return is_binary_tree_bst_helper(tree, float('-inf'), float('inf'))


if __name__ == '__main__':
    exit(generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv', is_binary_tree_bst))
