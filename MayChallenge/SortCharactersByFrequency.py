"""
May 22 Challenge - 451. Sort Characters By Frequency
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


INTUITION:
store character -> frequency in map
then store in heap and pop all

beats 96%
"""

import heapq


def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    hp = []
    count_map = {}
    res = ""
    for ch in s:
        if ch in count_map:
            count_map[ch] += 1
        else:
            count_map[ch] = 1

    for k, v in count_map.items():
        heapq.heappush(hp, (-v, k))

    while hp:
        num, ch = heapq.heappop(hp)
        res += ch * -num

    return res
