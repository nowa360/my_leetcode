"""
May 8 Challenge - Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

 Intuition:
Check slope of every point, but use cross product instead to avoid divide by 0 exception

 """


def checkStraightLine(coordinates):
    """
    :type coordinates: List[List[int]]
    :rtype: bool
    """
    n = len(coordinates)
    if n < 3:
        return True

    def is_cross_prod(pt1, pt2, pt3):
        return (pt1[1] - pt2[1]) * (pt3[0] - pt2[0]) == (pt3[1] - pt2[1]) * (pt1[0] - pt2[0])

    for i in xrange(2, n):
        if not is_cross_prod(coordinates[i], coordinates[i - 1], coordinates[i - 2]):
            return False

    return True
