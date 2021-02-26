"""
Feb 25 Challenge - Shortest Unsorted Continuous Subarray

Given an integer array nums, you need to find one continuous subarray
that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.



Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
"""


def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums_sorted = sorted(nums)

    start = 0
    end = len(nums) - 1
    while start < len(nums):
        if nums_sorted[start] != nums[start]:
            break
        start += 1

    if start == len(nums):
        return 0

    while end >= 0:
        if nums_sorted[end] != nums[end]:
            break
        end -= 1

    return end - start + 1