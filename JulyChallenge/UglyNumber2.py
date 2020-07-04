"""
Ugly Number II - July 4 Challenge

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp = [1 for _ in xrange(n)]

    idx2, idx3, idx5 = 0, 0, 0

    for i in xrange(1, n):
        dp[i] = min(dp[idx2] * 2, dp[idx3] * 3, dp[idx5] * 5)

        if dp[i] == dp[idx2] * 2:
            idx2 += 1
        if dp[i] == dp[idx3] * 3:
            idx3 += 1
        if dp[i] == dp[idx5] * 5:
            idx5 += 1
    return dp[-1]
