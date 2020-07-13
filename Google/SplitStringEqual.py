"""
Question 2:
Given a string S, we can split S into 2 strings: S1 and S2.
Return the number of ways S can be split such that the number of unique characters between S1 and S2 are the same.

Example 1:

Input: "aaaa"
Output: 3
Explanation: we can get a - aaa, aa - aa, aaa- a
Example 2:

Input: "bac"
Output: 0
Example 3:

Input: "ababa"
Output: 2
Explanation: ab - aba, aba - ba
"""


def splitString(s):
    if len(s) <= 1:
        return 1

    res = 0
    for i in xrange(len(s)):
        if set(s[:i]) == set(s[i:]):
            res += 1

    return res


print(splitString("aaaa"))  # expects 3
print(splitString("bac"))  # expects 0
print(splitString("ababa"))  # expects 2
