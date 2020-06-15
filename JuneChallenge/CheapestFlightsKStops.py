"""
June 14 Challenge - 787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the
cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Time: O((V + E) * log V)
Space: O(V^2)
"""
import collections
import heapq


def findCheapestPrice(n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """
    graph = collections.defaultdict(dict)
    visited = {}
    for source, destination, weight in flights:
        graph[source][destination] = weight
    heap = [(0, src, 0)]
    while heap:
        price, source, nth_move = heapq.heappop(heap)
        if source == dst and K >= nth_move - 1:
            return price
        if source not in visited or visited[source] > nth_move:
            visited[source] = nth_move
            for neighbor in graph[source]:
                heapq.heappush(heap, (graph[source][neighbor] + price, neighbor, nth_move + 1))
    return -1
