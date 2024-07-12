nums = [1, 2, 3, 4]
k = 5
left, right, operations = 0, len(nums) - 1, 0
while left < right:
    if nums[left] + nums[right] == k:
        operations += 1
        left += 1
        right -= 1
    elif nums[left] + nums[right] < k:
        left += 1
    else:
        right -= 1

print(operations)
