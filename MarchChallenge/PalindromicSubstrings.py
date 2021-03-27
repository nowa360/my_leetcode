"""
March 27 Challenge -  Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different
substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """

    def getCountSubStr(substr, start, end):
        count = 0
        while start >= 0 and end < len(substr) and substr[start] == substr[end]:
            start -= 1
            end += 1
            count += 1
        return count

    res = 0

    for i in xrange(len(s)):
        # for odd length
        res += getCountSubStr(s, i, i)
        # for even length
        res += getCountSubStr(s, i, i + 1)

    return res

