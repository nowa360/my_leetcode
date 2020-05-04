"""
Number Complement - May 4
Given a positive integer, output its complement number.
The complement strategy is to flip the bits of its binary representation.

Ex.1
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
and its complement is 010. So you need to output 2.


Ex.2
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits),
and its complement is 0. So you need to output 0.



"""


def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    res = ""
    for char in "{0:b}".format(num):
        if char == '1':
            res += "0"
        else:
            res += '1'
    return int(res, 2)
