"""
Jump Game  - Apr 25 Leetcode challenge

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
"""


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    last_idx = n - 1

    for i in xrange(n - 1):
        curr_idx = n - i - 2
        if nums[curr_idx] + curr_idx >= last_idx:
            last_idx = curr_idx
    return last_idx == 0
