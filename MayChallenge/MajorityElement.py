
"""
Majority Element

May 6 Challenge

Given an array of size n, find the majority element. The majority element is the element that appears more than
n/2 times

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        return nums[0]

    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
            if count_dict[num] > n / 2:
                return num
        else:
            count_dict[num] = 1


"""
fastest anonymous solution

import math
 def majorityElement(self, nums):
        user = dict((i,nums.count(i)) for i in set(nums))
        U = {}
        a = len(nums) // 2
        for key,value in user.items():
            if value>a:
                U[key] = value
        
        MX = max(U,key = U.get)
        return MX
"""