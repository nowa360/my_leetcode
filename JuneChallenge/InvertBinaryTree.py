"""
June 1 Challenge - Invert Binary Tree
"""


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root
