"""
July 23 Challenge - Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all
the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    count = {}
    res = [0, 0]
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    i = 0
    for k, v in count.items():
        if v == 1:
            res[i] = k
            i += 1

    return res
