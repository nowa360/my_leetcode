"""
June 27 Challenge - Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [float('inf') for _ in xrange(n + 1)]

    dp[0] = 0

    for i in xrange(1, n + 1):
        min_val = float('inf')
        j = 1
        while i - j ** 2 >= 0:
            min_val = min(min_val, dp[i - j ** 2] + 1)
            j += 1

        dp[i] = min_val

    return dp[n]
