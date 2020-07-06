"""
July 6 Challenge - Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    99
    """
    idx = len(digits) - 1
    while idx >= 0:
        if digits[idx] == 9:
            digits[idx] = 0
            idx -= 1
            has_carry = True
        else:
            digits[idx] += 1
            idx = -1
            has_carry = False

    return [1] + digits if has_carry else digits
