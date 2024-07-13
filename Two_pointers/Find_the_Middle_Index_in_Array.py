nums = [2,3,-1,8,4]

left_sum=0
right_sum=sum(nums)
for i, num in enumerate(nums):
    left_sum+=num
    if left_sum==right_sum:
        print(i)

    right_sum-=num

print(-1)










