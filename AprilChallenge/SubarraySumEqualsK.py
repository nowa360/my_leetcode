"""
Subarray Sum Equals K - Leetcode Challenge Apr 22

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum
equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    dic = {0: 1}
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum = curr_sum + num

        if curr_sum - k in dic:
            count = count + dic[curr_sum - k]

        if curr_sum in dic:
            dic[curr_sum] = dic[curr_sum] + 1
        else:
            dic[curr_sum] = 1

    return count
