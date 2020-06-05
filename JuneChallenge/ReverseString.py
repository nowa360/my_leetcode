"""
June 4 Challenge - Reverse String
"""


def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    for i in xrange(len(s) // 2):
        s[i], s[-1 - i] = s[-1 - i], s[i]
