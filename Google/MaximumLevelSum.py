"""
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
"""


def maxLevelSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    nex = [root]
    curr_max = float('-inf')
    res = curr_lvl = 1

    while nex:
        curr = nex
        curr_sum = sum([x.val for x in curr])
        if curr_sum > curr_max:
            curr_max = curr_sum
            res = curr_lvl

        nex = []

        for node in curr:
            if node.left:
                nex.append(node.left)
            if node.right:
                nex.append(node.right)
        curr_lvl += 1
    return res
