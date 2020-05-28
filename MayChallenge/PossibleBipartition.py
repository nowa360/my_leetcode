"""
May 27 Challenge - Possible Bi-partition
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].

INTUITION:

1) generate the graph
2) use two-coloring technique to check if bipartite
3) two-coloring technique using BFS
"""


import collections
from collections import deque


def possibleBipartition(N, dislikes):
    """
    :type N: int
    :type dislikes: List[List[int]]
    :rtype: bool
    """
    uncolored, color1, color2 = 0, 1, -1

    graph = collections.defaultdict(set)
    for u, v in dislikes:
        graph[u].add(v)
        graph[v].add(u)

    color_lst = [uncolored for _ in xrange(N + 1)]

    explored = set()
    q = deque()
    for i in xrange(1, N + 1):
        if i not in explored:
            q.append(i)
        while q:
            subject = q.popleft()

            if color_lst[subject] == uncolored:
                color_lst[subject] = color1

            to_color = -color_lst[subject]

            for disliked in graph[subject]:

                if color_lst[disliked] == color_lst[subject]:
                    return False

                color_lst[disliked] = to_color
                if disliked not in explored:
                    q.append(disliked)
                    explored.add(disliked)
    return True
