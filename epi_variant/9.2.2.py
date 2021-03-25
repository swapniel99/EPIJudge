from binary_tree_node import BinaryTreeNode


def k_balanced_binary_tree_helper(node: BinaryTreeNode, k: int):
    if node is None:
        return True, 0, None

    leftb, leftn, leftres = k_balanced_binary_tree_helper(node.left, k)
    rightb, rightn, rightres = k_balanced_binary_tree_helper(node.right, k)

    balanced = leftb and rightb and abs(leftn - rightn) <= k
    nodes = leftn + rightn + 1
    res = node if not balanced and leftb and rightb else leftres or rightres

    return balanced, nodes, res


def is_k_balanced_binary_tree(tree: BinaryTreeNode, k: int) -> bool:
    return k_balanced_binary_tree_helper(tree, k)[-1]
