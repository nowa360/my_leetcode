"""
482. License Key Formatting
https://leetcode.com/problems/license-key-formatting/
"""


def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    res = ""
    count = 0
    for i in xrange(len(S) - 1, -1, -1):
        if count == K:
            res += '-'
            count = 0
        if S[i].isalnum():
            res += S[i].upper()
            count += 1
    return res.rstrip("-")[::-1]