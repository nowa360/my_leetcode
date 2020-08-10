"""
August 10 Challenge - Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""


def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    col = 0
    po = 0
    for i in xrange(len(s) - 1, -1, -1):
        col += (ord(s[i]) - ord('A') + 1) * (26 ** po)
        po += 1

    return col
