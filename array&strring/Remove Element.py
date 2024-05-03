def removeElement( nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0

    for i in nums:
        if i != val:
            nums[k] = i
            k += 1

    return k




nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))