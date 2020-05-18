"""
May 18 Challenge - Permutation in String


Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""


def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    s1_map = [0 for _ in xrange(26)]
    s2_map = [0 for _ in xrange(26)]

    for char in s1:
        s1_map[ord(char) - ord('a')] += 1

    i, j = 0, 0
    while j < len(s2):
        s2_map[ord(s2[j]) - ord('a')] += 1

        if len(s1) == j - i + 1:

            if s1_map == s2_map:
                return True
            s2_map[ord(s2[i]) - ord('a')] -= 1
            i += 1
        j += 1

    return False
