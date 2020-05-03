"""
May 3 Challenge
https://leetcode.com/problems/ransom-note/

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    mag_dict = {}
    for char in magazine:
        if char in mag_dict:
            mag_dict[char] += 1
        else:
            mag_dict[char] = 1

    for char in ransomNote:
        if char not in mag_dict or mag_dict[char] == 0:
            return False
        else:
            mag_dict[char] -= 1

    return True
