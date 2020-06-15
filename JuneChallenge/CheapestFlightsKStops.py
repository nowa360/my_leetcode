"""
June 14 Challenge - 787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the
cheapest price from src to dst with up to k stops. If there is no such route, output -1.
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
    price_map = collections.defaultdict(dict)
    for start, end, price in flights:
        price_map[start][end] = price
    heap = [(0, src, K + 1)]
    while heap:
        price, cur_city, allowed_k = heapq.heappop(heap)
        if cur_city == dst:
            return price
        if allowed_k > 0:
            for dest in price_map[cur_city]:
                heapq.heappush(heap, (price + price_map[cur_city][dest], dest, allowed_k - 1))
    return -1
