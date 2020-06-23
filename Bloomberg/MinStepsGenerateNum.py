"""
Given an int n. You can use only 2 operations:

multiply by 2
integer division by 3 (e.g. 10 / 3 = 3)
Find the minimum number of steps required to generate n from 1.

Example 1:

Input: 10
Output: 6
Explanation: 1 * 2 * 2 * 2 * 2 / 3 * 2
6 steps required, as we have used 5 multiplications by 2, and one division by 3.
Example 2:

Input: 3
Output: 7
Explanation: 1 * 2 * 2 * 2 * 2 * 2 / 3 / 3
7 steps required, as we have used 5 multiplications by 2 and 2 divisions by 3.
"""

from collections import deque


def min_steps(n):
    que = deque([1])
    total_steps = 0

    while que:

        total_steps += 1

        for i in xrange(len(que)):

            curr_num = que.popleft()

            divide_3 = int(curr_num / 3)
            mult_2 = int(curr_num * 2)

            if divide_3 == n or mult_2 == n:
                return total_steps

            que.append(mult_2)

            if divide_3 > 0:
                que.append(divide_3)


print(min_steps(10))  # expects 6
print(min_steps(3))  # expects 7
