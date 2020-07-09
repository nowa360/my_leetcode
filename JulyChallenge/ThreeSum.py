"""
July 8 Challenge - 3 Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    nums.sort()
    prev = None
    res = []
    print(nums)
    for i, num in enumerate(nums):
        if num == prev:
            continue
        prev = num

        l, r = i + 1, len(nums) - 1
        while l < r:
            curr_triple = [num, nums[l], nums[r]]
            curr_sum = sum(curr_triple)
            if curr_sum == 0:
                res.append(curr_triple)
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif curr_sum > 0:
                r -= 1
            else:
                l += 1
    return res
