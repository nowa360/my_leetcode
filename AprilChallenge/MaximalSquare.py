import copy


def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int

    Apr.27 Challenge
    221. Maximal Square - M
    https://leetcode.com/problems/maximal-square/

    Dynamic Programming

   1 1 0
   1 2 1
   0 1 1 -> 2

    2 1
    0 1 -> 1

    1
    1 -> 1

    0
    1 -> 1


    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    1 0 1 0
    1 0 1 1
    1 0 1 1
    1 1 1 1

    diag_prev    dp[c]
    dp[c-1]      curr

    m = row
    n = col
    runtime: O(mn)
    memory: O(m)

    runtime: faster than 58.62% of all submissions
    memory: less than 12.50% of all submissions
    TODO: can improve without deepcopy

    """
    if not matrix or matrix == []:
        return 0

    rows = len(matrix[0])
    dp, curr_dp = [0 for _ in xrange(rows)], [0 for _ in xrange(rows)]
    curr_max, diag_prev = 0, 0

    for r, row in enumerate(matrix):
        for c, num in enumerate(row):
            num = int(num)
            if c != 0 and num == 1:
                curr_dp[c] = min(dp[c], dp[c - 1], curr_dp[c - 1]) + 1
                # print(dp[c], dp[c - 1], diag_prev)
                curr_max = max(curr_dp[c], curr_max)
            elif num == 1:
                curr_max = max(num, curr_max)
                curr_dp[c] = num
            else:
                curr_dp[c] = num

        # print(curr_dp, dp)
        dp = copy.copy(curr_dp)

    return curr_max * curr_max
