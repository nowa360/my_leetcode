"""
Valid Perfect Square - May 9 Challenge
https://leetcode.com/problems/valid-perfect-square/

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false


Intuition:
Use binary search
"""


def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    left, right = 0, num

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > num:
            right = mid - 1
        elif mid * mid < num:
            left = mid + 1
        else:
            return True

    return False
