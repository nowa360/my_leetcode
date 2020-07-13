"""
Google OA

Question 1:
Given an Array A, find the minimum amplitude you can get after changing up to 3 elements.
Amplitude is the range of the array (basically difference between largest and smallest element).

Example 1:

Input: [-1, 3, -1, 8, 5 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5
Example 2:

Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10
"""


def minAmp(nums):
    nums.sort()
    # change all 3 to the same number
    if len(nums) <= 3:
        return 0
    res = nums[-1] - nums[0]

    # min range should be found in [0, -3] , [1, -2], [2, -1]
    return min(res,
               nums[-4] - nums[0],
               nums[-3] - nums[1],
               nums[-2] - nums[2],
               nums[-1] - nums[3])


def minAmp2(nums):
    nums.sort()
    if len(nums) <= 3:
        return 0
    ans = nums[-1] - nums[0]
    i, j = 0, len(nums) - 4
    while j < len(nums):
        print(i, j)
        ans = min(ans, nums[j] - nums[i])
        i += 1
        j += 1
    return ans


print(minAmp([-1, 3, -1, 8, 5, 4]))  # expects 2
print(minAmp([10, 10, 3, 4, 10]))  # expects 0
