"""
May 25 Challenge - Uncrossed Lines

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Intuition:

If A[ y ] == B[ x ]:
DP[ y ][ x ] = DP[ y-1 ][ x-1 ] + 1

If A[ y ] != B[ x ]:
DP[ y ][ x ] = Max( DP[ y ][ x-1 ], DP[ y-1 ][ x ] )
"""


def maxUncrossedLines(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    dp = [[0 for _ in xrange(len(B))] for _ in xrange(len(A))]

    for i in xrange(len(A)):
        for j in xrange(len(B)):
            top = float('-inf') if i == 0 else dp[i - 1][j]
            left = float('-inf') if j == 0 else dp[i][j - 1]
            diag = 0 if i == 0 or j == 0 else dp[i - 1][j - 1]

            # (0,0) case
            if i == 0 and j == 0:
                top, left = 0, 0

            maxi = max(top, left)

            dp[i][j] = diag + 1 if A[i] == B[j] else maxi

    return dp[-1][-1]
