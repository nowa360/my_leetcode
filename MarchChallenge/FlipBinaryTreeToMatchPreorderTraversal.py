"""
Mar 29 Challenge - 971. Flip Binary Tree To Match Preorder Traversal

https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n.
You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Any node in the binary tree can be flipped by swapping its left and right subtrees.
For example, flipping node 1 will have the following effect:


Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. You may return the answer in any order.
If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].



"""


def flipMatchVoyage(root, voyage):
    """
    :type root: TreeNode
    :type voyage: List[int]
    :rtype: List[int]
    """
    res = []
    stack = [root]
    i = 0
    while stack:
        node = stack.pop()
        if not node: continue
        if node and node.val != voyage[i]:
            return [-1]
        i += 1
        if node.right and node.right.val == voyage[i]:
            if node.left:
                res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        else:
            stack.append(node.right)
            stack.append(node.left)
    return res
