"""
May 31 Challenge - Edit Distance
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Approach 1 DP

"""
from heapq import heappush, heappop


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    dp = [[0 for x in range(len(word2) + 1)] for y in range(len(word1) + 1)]

    for i in xrange(len(word1) + 1):
        dp[i][0] = i

    for i in xrange(len(word2) + 1):
        dp[0][i] = i

    for i in xrange(1, len(word1) + 1):
        for j in xrange(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i - 1][j],  # remove
                                   dp[i][j - 1],  # insert
                                   dp[i - 1][j - 1])  # replace

    return dp[-1][-1]


def minDistance2(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    heap = [(0, word1, word2)]
    visited = set()
    while heap:
        d, w1, w2 = heappop(heap)
        if (w1, w2) in visited:
            continue
        visited.add((w1, w2))
        if w1 == w2:
            return d
        if w1 and w2 and w1[0] == w2[0]:
            heappush(heap, (d, w1[1:], w2[1:]))
        else:
            if w1:
                heappush(heap, (d + 1, w1[1:], w2))  # delete
            if w1 and w2:
                heappush(heap, (d + 1, w1[1:], w2[1:]))  # replace
            if w2:
                heappush(heap, (d + 1, w1, w2[1:]))  # add
    print(set)
