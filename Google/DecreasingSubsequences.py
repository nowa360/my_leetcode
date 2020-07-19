"""
Decreasing Subsequences

Given an int array nums of length n. Split it into strictly decreasing subsequences.
Output the min number of subsequences you can get by splitting.

Example 1:

Input: [5, 2, 4, 3, 1, 6]
Output: 3
Explanation:
You can split this array into: [5, 2, 1], [4, 3], [6]. And there are 3 subsequences you get.
Or you can split it into [5, 4, 3], [2, 1], [6]. Also 3 subsequences.
But [5, 4, 3, 2, 1], [6] is not legal because [5, 4, 3, 2, 1] is not a subsequence of the original array.
Example 2:

Input: [2, 9, 12, 13, 4, 7, 6, 5, 10]
Output: 4
Explanation: [2], [9, 4], [12, 10], [13, 7, 6, 5]
Example 3:

Input: [1, 1, 1]
Output: 3
Explanation: Because of the strictly descending order you have to split it into 3 subsequences: [1], [1], [1]


Time complexity: O(nlogn).
Space complexity: O(n).

INSTINCT:

Quoting MikeBonzai:
The number of decreasing subsequence partitions is equal to the length of the
longest non-decreasing subsequence,  because every non-decreasing number represents a point where a continuation of a
previous decreasing subsequence is impossible.

Therefore, this question is similar to Longest Increasing Subsequence (#300)
https://leetcode.com/problems/longest-increasing-subsequence/
"""


def lengthOfNonDecreasingSubsequence(sequence):
    if not sequence:
        return 0

    dp = [1 for _ in xrange(len(sequence))]
    curr_max = 1

    for i in xrange(1, len(sequence)):

        for j in xrange(i):

            if sequence[i] >= sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

        curr_max = max(curr_max, dp[i])

    return curr_max
