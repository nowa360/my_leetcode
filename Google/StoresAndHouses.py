"""
Stores and Houses

You are given 2 arrays representing integer locations of stores and houses
(each location in this problem is one-dementional). For each house, find the store closest to it.
Return an integer array result where result[i] should denote the location of the store closest to the i-th house.
If many stores are equidistant from a particular house, choose the store with the smallest numerical location.
Note that there may be multiple stores and houses at the same location.

Example 1:

Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
Output: [5, 11, 16]
Explanation:
The closest store to the house at location 5 is the store at the same location.
The closest store to the house at location 10 is the store at the location 11.
The closest store to the house at location 17 is the store at the location 16.
Example 2:

Input: houses = [2, 4, 2], stores = [5, 1, 2, 3]
Output: [2, 3, 2]
Example 3:

Input: houses = [4, 8, 1, 1], stores = [5, 3, 1, 2, 6]
Output: [3, 6, 1, 1]
"""


def stores_and_houses(houses, stores):
    def bin_search(num, store_lst):
        stores.sort()
        left, right = 0, len(stores) - 1
        min_dist = float('inf')
        res = 0

        while left <= right:
            mid = left + (right - left) / 2
            if store_lst[mid] == num:
                return store_lst[mid]
            else:

                curr_dist = abs(house - store_lst[mid])
                if curr_dist == min_dist:
                    res = min(res, store_lst[mid])
                elif curr_dist < min_dist:
                    res = store_lst[mid]
                    min_dist = curr_dist

                if stores[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
        return res

    for i, house in enumerate(houses):
        houses[i] = bin_search(house, stores)

    return houses


print(stores_and_houses([5, 10, 17], [1, 5, 20, 11, 16]))  # [5, 11, 16]
print(stores_and_houses([2, 4, 2], [5, 1, 2, 3]))  # [2, 3, 2]
print(stores_and_houses([4, 8, 1, 1],  [5, 3, 1, 2, 6]))  # [3, 6, 1, 1]
