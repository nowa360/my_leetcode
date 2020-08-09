import collections

"""
August 9 Challenge - Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1 instead.
"""


def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    que = collections.deque()
    fresh = 0

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 2:
                que.appendleft((r, c))
            elif val == 1:
                fresh += 1

    if fresh == 0:
        return 0
    time = 0
    trav = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    length, width = len(grid), len(grid[0])
    while que:
        time += 1
        for _ in xrange(len(que)):
            coord = que.pop()
            for a, b in trav:
                x = coord[0] + a
                y = coord[1] + b

                if x < 0 or y < 0 or x >= length or y >= width or grid[x][y] in (0, 2):
                    continue

                grid[x][y] = 2
                que.appendleft((x, y))
                fresh -= 1

    if fresh == 0:
        return time - 1
    else:
        return -1
