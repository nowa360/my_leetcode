def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    if target > nums[r]:
        return r + 1
    elif target <= nums[0]:
        return 0

    while l < r:
        mid = l + (r - l) // 2
        print(l, mid, r)
        if target > nums[mid]:
            if l == mid:
                return l + 1
            l = mid
        elif target < nums[mid]:
            if r == mid:
                return r
            r = mid
        else:
            return mid
