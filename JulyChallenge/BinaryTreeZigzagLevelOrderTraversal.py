"""
July 22 Challenge - Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []

    nex = [root]
    res = []
    curr = []
    in_order = True

    while nex:

        if in_order:
            res.append([x.val for x in nex[::-1]])
        else:
            res.append([x.val for x in nex])
        curr = nex
        nex = []
        for node in curr:

            if node.right:
                nex.append(node.right)

            if node.left:
                nex.append(node.left)
        if in_order:
            in_order = False
        else:
            in_order = True

    return res
