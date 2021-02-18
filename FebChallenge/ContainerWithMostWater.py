"""
Feb 17 Challenge - Letter Case Permutation

https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines,
which, together with the x-axis forms a container,
such that the container contains the most water.

"""


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i, j = 0, len(height) - 1
    area = 0

    while i < j:

        area = max(area, min(height[i], height[j]) * (j - i))

        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return area
