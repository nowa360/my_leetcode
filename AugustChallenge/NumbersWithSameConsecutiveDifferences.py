"""
August 18 Challenge - Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute difference between every
two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself.
For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

1 <= N <= 9
0 <= K <= 9
"""


def numsSameConsecDiff(N, K):
    """
    :type N: int
    :type K: int
    :rtype: List[int]
    """

    def dfs(n, k, lst, num):
        if n == 0:
            lst.append(num)
            return

        for i in xrange(10):
            if i == 0 and num == 0:
                continue
            elif num == 0:
                dfs(n - 1, k, lst, i)
            elif abs(num % 10 - i) == k:
                dfs(n - 1, k, lst, num * 10 + i)

    res = []

    if N == 0:
        return []
    elif N == 1:
        res.append(0)

    dfs(N, K, res, 0)
    return res
