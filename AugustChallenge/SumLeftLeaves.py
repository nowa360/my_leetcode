"""
August 24 Challenge - Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


def sumOfLeftLeaves(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def left_helper(node):

        count = 0
        if not node:
            return count

        if node.left:
            if not node.left.left and not node.left.right:
                count += node.left.val
            else:
                count += left_helper(node.left)

        if node.right:
            count += left_helper(node.right)

        return count

    return left_helper(root)

