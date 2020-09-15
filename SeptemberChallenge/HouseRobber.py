"""
Sept 14 Challenge - House Robber
"""


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    n = len(nums)
    dp = [0] * n

    if not nums:
        return 0

    if n >= 1:
        dp[0] = nums[0]

    if n >= 2:
        dp[1] = max(nums[1], nums[0])

    if n >= 3:
        for i in xrange(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[-1]
