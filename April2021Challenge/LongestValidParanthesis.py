"""
Longest Valid Parentheses - Apr 3, 2021 Challenge

Given a string containing just the characters '(' and ')',
 find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""


def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int

    DP IDEA:

    If s[i] is '(', set longest[i] to 0,because any string end with '(' cannot be a valid one.

    Else if s[i] is ')'

        If s[i-1] is '(', longest[i] = longest[i-2] + 2

        Else if s[i-1] is ')' and s[i-longest[i-1]-1] == '(', longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

    """

    if len(s) <= 1:
        return 0

    dp = [0 for _ in xrange(len(s))]
    curr_max = 0

    for i, val in enumerate(s):
        if val == ')':
            if i - 1 >= 0 and s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
                curr_max = max(curr_max, dp[i])
            else:
                # if val == (
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
                    curr_max = max(curr_max, dp[i])
        # else if s[i] == '(', skip it, because longest[i] must be 0

    return curr_max
