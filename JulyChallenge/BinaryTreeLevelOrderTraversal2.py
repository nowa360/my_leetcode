"""
July 2 Challenge - Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

"""


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    prev = [root]
    res = []
    while prev:
        res.append([n.val for n in prev])
        curr = []
        for node in prev:
            if node.left:
                curr.append(node.left)
            if node.right:
                curr.append(node.right)
        prev = curr
    return list(reversed(res))
