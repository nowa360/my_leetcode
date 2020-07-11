"""
July 11 Challenge - Subset

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = [[]]

    for num in nums:
        for i in xrange(len(results)):
            subset = results[i] + [num]
            results.append(subset)

    return results
