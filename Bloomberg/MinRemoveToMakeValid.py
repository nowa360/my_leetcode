"""
1249. Minimum Remove to Make Valid Parentheses
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""


def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    balance = 0
    for char in s:
        if balance <= 0 and char == ")":
            continue
        elif char == ")":
            stack.append(char)
            balance -= 1
        elif char == "(":
            stack.append(char)
            balance += 1
        else:
            stack.append(char)

    temp_stack = []

    while balance != 0:
        char = stack.pop()
        if char == "(":
            balance -= 1
            continue
        else:
            temp_stack.append(char)

    while temp_stack:
        stack.append(temp_stack.pop())

    return "".join(stack)
