# coding=utf-8
"""
August 12 Challenge -  Pascal's Triangle II

Solution
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = [0 for _ in xrange(rowIndex + 1)]
    res[0] = 1

    for i in xrange(1, rowIndex + 1):
        for j in xrange(i, 0, -1):
            res[j] = res[j] + res[j - 1]
    return res
