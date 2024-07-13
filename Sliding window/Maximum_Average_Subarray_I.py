nums = [1,12,-5,-6,50,3]
k = 4
if len(nums) < k or k <= 0:
    print( None ) # Handle edge cases where input is invalid

window_sum = sum(nums[:k])
window_average = window_sum / k
for i in range(len(nums) - k):
    window_sum = window_sum - nums[i] + nums[i + k]
    window_average = max(window_average, window_sum / k)

print(window_average)