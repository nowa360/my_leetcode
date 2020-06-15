"""Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in
this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""


def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dp = [1 for _ in xrange(len(nums))]

    nums.sort()
    for i in xrange(len(nums) - 1):
        for j in xrange(i + 1, len(nums)):
            if nums[j] % nums[i] == 0:
                dp[j] += 1

    max_num = nums.index(max(nums))

    res = []

    for num in nums:
        if max_num % num == 0:
            res.append(num)
    return num
