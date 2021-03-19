from binary_tree_node import BinaryTreeNode


def largest_complete_helper(node: BinaryTreeNode):
    if node is None:
        return True, True, 0, 0, 0

    perleft, compleft, htleft, szleft, resleft = largest_complete_helper(node.left)
    perright, compright, htright, szright, resright = largest_complete_helper(node.right)

    perfect = perleft and perright and htleft == htright
    complete = perfect \
        or (perleft and compright and htleft == htright) \
        or (compleft and perright and htleft == htright + 1)
    height = max(htleft, htright) + 1
    size = szleft + szright + 1
    res = size if complete else max(resleft, resright)

    return perfect, complete, height, size, res


def isCompleteTree(root: BinaryTreeNode) -> int:
    return largest_complete_helper(root)[-1]
