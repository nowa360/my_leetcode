"""
May 12 Challenge - Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
element which appears exactly once. Find this single element that appears only once.

https://leetcode.com/problems/single-element-in-a-sorted-array/

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10


Note: Your solution should run in O(log n) time and O(1) space.

INTUITION:
If mid is even, its pair should be mid + 1 supposedly
If mid is off, its pair is mid - 1 supposedly
So check the later half, otherwise if not satisfied, check prior half
"""


def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) / 2
        if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
            left = mid + 1
        else:
            right = mid
    return nums[left]
