"""
June 15 Challenge
700. Search in a Binary Search Tree

"""


def searchBST(root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if not root:
        return None
    if root.val == val:
        return root
    elif val > root.val:
        return searchBST(root.right, val)
    else:
        return searchBST(root.left, val)
