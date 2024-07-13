nums =[1,1,1,0,0,0,1,1,1,1,0]
k=2

maximum=0
left=0

zeros=0

for right in range(len(nums)):

    if nums[right]==0:
        zeros+=1

    while zeros > k:
        if nums[left] == 0:
            zeros -= 1

        left+=1

    maximum=max(maximum,right-left+1)
