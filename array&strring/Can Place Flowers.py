def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if n==0:
        return True
    for i in range(len(flowerbed)):
        if(i==0 or flowerbed[i-1]==0) and flowerbed[i]==0 and (i==len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i]=1
            n-=1
            if n==0:
                return True
    return False







flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))