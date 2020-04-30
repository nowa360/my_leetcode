"""
Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
Apr.30
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/

Given a binary tree where each path
going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree.

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the
nodes along a path results in a sequence in the given binary tree.


Example 1:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation:
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
Other valid sequences are:
0 -> 1 -> 1 -> 0
0 -> 0 -> 0


Example 2:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.


Example 3:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.


Constraints:

1 <= arr.length <= 5000
0 <= arr[i] <= 9
Each node's value is between [0 - 9].
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidSequence(root, arr):
    """
    :type root: TreeNode
    :type arr: List[int]
    :rtype: bool
    """

    def dfs(node, sub_arr):
        length = len(sub_arr)
        if node and node.val == sub_arr[0]:
            if length == 1 and not node.left and not node.right:
                return True
            elif length > 1:
                left = False if not node.left else dfs(node.left, sub_arr[1:])
                right = False if not node.right else dfs(node.right, sub_arr[1:])
                return left or right
            else:
                return False
        else:
            return False

    return dfs(root, arr)
