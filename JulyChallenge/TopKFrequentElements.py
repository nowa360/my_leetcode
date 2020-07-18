# coding=utf-8
"""
Top K Frequent Elements

Solution
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freq = {}
    freq_as_key = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    for num, v in freq.iteritems():
        if v not in freq_as_key:
            freq_as_key[v] = {num}
        else:
            freq_as_key[v].add(num)

    curr_freq = len(nums)
    res = []

    while curr_freq > 0 and len(res) < k:
        if curr_freq in freq_as_key:
            for ele in freq_as_key[curr_freq]:
                res.append(ele)

        curr_freq -= 1

    return res[:k]