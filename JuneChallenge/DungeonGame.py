"""
June 21 Challenge - Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and
must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0
or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each
step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal
path RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K) | -3  | 3
-5    | -10 | 1
10    | 30  | -5 (P)
"""


def calculateMinimumHP(dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    m = len(dungeon)
    n = len(dungeon[0])

    dp = [[0 for _ in xrange(n)] for _ in xrange(m)]

    for i in xrange(m - 1, -1, -1):
        for j in xrange(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dp[i][j] = max(1, 1 - dungeon[i][j])
            elif i == m - 1:
                dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
            elif j == n - 1:
                dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
            else:
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
    return dp[0][0]