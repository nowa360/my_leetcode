"""
July 18 Challenge - Course Schedule II


"""
import collections


def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]

    JenningsWG DFS solution
    """
    res = []
    graph = collections.defaultdict(list)  # a graph for all courses
    for pre in prerequisites:
        graph[pre[0]].append(pre[1])
    visited = [0 for _ in xrange(numCourses)]
    # -1: visited
    # 0~: iteration pointer
    stack = []
    for x in xrange(numCourses):
        if visited[x] == -1: continue
        stack.append(x)
        while stack:
            tmp = stack[-1]
            v = visited[tmp]
            visited[tmp] += 1
            if v < len(graph[tmp]):
                pre = graph[tmp][v]
                if visited[pre] == 0:
                    stack.append(pre)
                elif visited[pre] > 0:
                    return []
            else:
                res.append(stack.pop())
                visited[tmp] = -1
    return res