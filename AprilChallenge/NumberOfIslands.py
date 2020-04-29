"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Apr.17 challenge


Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    def dfs(x, y, matrix):
        if (x < 0 or x >= len(matrix) or
                y < 0 or y >= len(matrix[0]) or
                matrix[x][y] == "0"):
            return
        matrix[x][y] = "0"
        dfs(x - 1, y, matrix)
        dfs(x + 1, y, matrix)
        dfs(x, y - 1, matrix)
        dfs(x, y + 1, matrix)

    count = 0

    if len(grid) == 0:
        return count

    for rc, row in enumerate(grid):
        for cc, num in enumerate(row):
            if num == "1":
                dfs(rc, cc, grid)
                count += 1
    return count


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(numIslands(grid))  # expects 1
