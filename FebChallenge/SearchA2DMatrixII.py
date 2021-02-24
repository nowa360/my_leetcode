"""
Feb 23 Challenge -  Search a 2D Matrix II

Write an efficient algorithm that searches for a target value in an m x n integer matrix.
The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false



INSTINCT: START FROM TOP RIGHT
"""


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, cols - 1

    while r < rows and c >= 0:
        if target > matrix[r][c]:
            r += 1
        elif target < matrix[r][c]:
            c -= 1
        else:
            return True

    return False
