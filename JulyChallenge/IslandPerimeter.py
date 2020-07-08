"""
July 7 Challenge - 463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
 and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
"""


class IslandPerimeter(object):

    def __init__(self):
        self.visited = set()

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def do_traverse(y, x):
            count = 0

            if (x, y) in self.visited:
                return count

            self.visited.add((x, y))

            # if it borders left, right
            if x == 0:
                count += 1
            if x == len(grid[0]) - 1:
                count += 1

            # if it borders top, bottom
            if y == 0:
                count += 1
            if y == len(grid) - 1:
                count += 1

            for add_x, add_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + add_x, y + add_y
                if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                    if grid[new_y][new_x] == 0:
                        count += 1
                    # it's a land
                    else:
                        count += do_traverse(new_y, new_x)

            return count

        for ri, row in enumerate(grid):
            for ci, sq in enumerate(row):
                if sq == 1:
                    return do_traverse(ri, ci)

        return 0
