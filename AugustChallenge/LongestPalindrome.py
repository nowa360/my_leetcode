"""
August 14 Challenge - Longest Palindrome

Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    track = set()
    for ch in s:
        if ch in track:
            track.remove(ch)
            res += 2
        else:
            track.add(ch)
    return res + 1 if len(track) > 0 else res
