"""
May 21 Challenge - Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.


Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.


Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""


def countSquares(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """

    def do_compute(x, y, matrix):
        diag = matrix[x - 1][y - 1] if y > 0 and x > 0 else 0
        left = matrix[x][y - 1] if y > 0 else 0
        top = matrix[x - 1][y] if x > 0 else 0
        matrix[x][y] = min(diag, left, top) + 1

        return matrix[x][y]

    total = 0

    for i, lst in enumerate(matrix):
        for j, num in enumerate(lst):
            if num == 1:
                total += do_compute(i, j, matrix)

    return total
