"""
First Unique Character in a String
May 5 Challenge

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    s_dict = {}
    for i, char in enumerate(s):
        if char not in s_dict:
            s_dict[char] = i
        else:
            s_dict[char] = -1

    for char in s:
        if char in s and s_dict[char] != -1:
            return s_dict[char]

    return -1
