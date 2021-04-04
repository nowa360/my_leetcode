"""
March 30 Challenge - 354 Russian Doll Envelopes

https://leetcode.com/problems/russian-doll-envelopes/

Also refer LIS problem
https://leetcode.com/problems/longest-increasing-subsequence/


You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of
an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the
other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1


Constraints:

1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 104
"""


def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """

    # sort by width, then by height decreasing
    sorted_nums = sorted(envelopes, key=lambda x: (x[0], -x[1]))

    # Longest Increasing Subsequence problem from here
    # This solution uses DP in O(N^2)
    # There is a better solution using Patience sorting with  N Log N

    dp = [1 for _ in xrange(len(sorted_nums))]

    for i in xrange(len(sorted_nums)):
        for j in xrange(i):
            if sorted_nums[i][1] > sorted_nums[j][1]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)
