def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if not s:
        return True
    s_ptr = 0
    for char in t:
        if s_ptr == len(s):
            return True
        if char == s[s_ptr]:
            s_ptr += 1
    return s_ptr == len(s)