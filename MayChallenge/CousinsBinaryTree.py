"""
Cousins in Binary Tree
May 7 Challenge


In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.


My Algorithm: Calculate depth of each x and y and also record the parent value if found

"""


def isCousins(root, x, y):
    """
    :type root: TreeNode
    :type x: int
    :type y: int
    :rtype: bool
    """

    def dfs(node, value, depth, parent):
        if not node:
            return None
        elif node.val == value:
            return depth, parent  # assumed type tuple

        left = dfs(node.left, value, depth + 1, node.val)
        right = dfs(node.right, value, depth + 1, node.val)

        return left if left else right

    x_tuple = dfs(root, x, 1, None)
    y_tuple = dfs(root, y, 1, None)

    return x_tuple[0] == y_tuple[0] and x_tuple[1] != y_tuple[1]
