"""
June 29 Challenge - 62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m < 1 or n < 1:
        return 0

    dp = [1 for _ in xrange(m)]

    for row in xrange(1, n):
        prev = 1
        for col in xrange(1, m):
            curr = prev + dp[col]
            prev = curr
            dp[col] = curr

    return dp[-1]
