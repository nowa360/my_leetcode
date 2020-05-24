from Libraries.TreeNode import TreeNode

"""
May 24 Challenge
Construct Binary Search Tree from Pre-order Traversal


Return the root node of a binary search tree that matches the given pre-order traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left 
has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a pre-order 
traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree 
with the given requirements.
"""

def bstFromPreorder(preorder):
    """
    :type preorder: List[int]
    :rtype: TreeNode
    """
    root = TreeNode(preorder[0])
    stack = [root]

    for num in preorder[1:]:
        curr = stack[-1]
        node = TreeNode(num)
        while stack and stack[-1].val < node.val:
            curr = stack[-1]
            stack.pop()
        if curr.val < node.val:
            curr.right = node
        else:
            curr.left = node

        stack.append(node)
    return root
